const express = require("express")
const { graphqlHTTP } = require("express-graphql")
const { buildSchema } = require("graphql")
const path = require("path");
const crypto = require('crypto');

const STRENGTH_CHALLENGE = 999;
const NUM_CHALLENGE = 40;
const ERROR_MSG = "Wrong !!!";
const CORRECT_MSG = "OK !!!";

// Currently support admin only
var otps = Object.create(null);
otps["admin"] = Object.create(null);
function genOtp(ip, force = false) {
  if (force || !otps["admin"][ip]) {
    function intToString(v) {
      let s = v.toString();
      while (s.length !== STRENGTH_CHALLENGE.toString().length) s = '0' + s;
      return s;
    }
    const otp = [];
    for (let i = 0; i < NUM_CHALLENGE; ++i) 
      otp.push(
        intToString(crypto.randomInt(0, STRENGTH_CHALLENGE))
      );
    otps["admin"][ip] = otp;
  }
}

const rateLimiter = require('express-rate-limit')({
  windowMs: 30 * 60 * 1000,
  max: 5,
  standardHeaders: true,
  legacyHeaders: false,
  onLimitReached: async (req) => genOtp(req.ip, true)
});

function checkOtp(username, ip, idx, otp) {
  if (!otps[username]) return false;
  if (!otps[username][ip]) return false;
  return otps[username][ip][idx] === otp;
}

// Construct a schema, using GraphQL schema language
const schema = buildSchema(`
  type Query {
    otp(u: String!, i: Int!, otp: String!): String!
  }
`);

// The root provides a resolver function for each API endpoint
const root = {
  otp: ({ u, i, otp }, req) => {
    if (i >= NUM_CHALLENGE || i < 0) return ERROR_MSG;
    if (!checkOtp(u, req.ip, i, otp)) return ERROR_MSG;
    rateLimiter.resetKey(req.ip);
    otps[u][req.ip][i] = 1;
    return CORRECT_MSG;
  },
}

const app = express();

// For monitor cheaters :)
app.use((req, res, next) => {
  console.log(`[ ${new Date()} ] - [ ${req.ip} ] - [ ${req.method} ] - [ ${req.url} ]`);
  next();
})

// Secure WAF !!!!
const { isDangerousPayload, isDangerousValue } = require('./waf');
app.use((req, res, next) => {
  if (isDangerousValue(req.url)) return res.send(ERROR_MSG);
  if (isDangerousPayload(req.query)) return res.send(ERROR_MSG);
  next();
});

app.use((req, res, next) => { genOtp(req.ip); next() });
app.use(require('body-parser').json({ limit: '128b' }));
app.use(
  "/graphql",
  rateLimiter,
  graphqlHTTP({
    schema: schema,
    rootValue: root,
  })
);

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, "views", "index.html"));
});

app.get('/admin', (req, res) => {
  let sum = 0;
  for (let i = 0; i < NUM_CHALLENGE; ++i)
    sum += otps["admin"][req.ip][i];
  res.send((sum === NUM_CHALLENGE) ? process.env.FLAG : ERROR_MSG);
});

app.listen(4000)
console.log("Running a GraphQL API server at http://localhost:4000/graphql")
