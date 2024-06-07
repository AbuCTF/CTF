function isDangerousValue(s) {
  return s.includes('admin') || s.includes('\\'); // Linux does not need to support "\"
}

/** Secured WAF for admin on Linux
*/
function isDangerousPayload(obj) {
  if (!obj) return false;
  const keys = Object.keys(obj);
  for (let i = 0; i < keys.length; ++i) {
    const key = keys[i];
    if (isDangerousValue(key)) return true;
    if (typeof obj[key] === 'object') {
      if (isDangerousPayload(obj[key])) return true;
    } else {
      const val = obj[key].toString();
      if (isDangerousValue(val)) return true;
    }
  }
  return false;
}

module.exports = {
  isDangerousValue,
  isDangerousPayload,
}
