import random
random.seed(1337)
ops = [
    lambda x: x+3,
    lambda x: x-3,
    lambda x: x*3,
    lambda x: x^3,
]

flag = list(open("flag.txt", "rb").read())
out = []
for v in flag:
    out.append(random.choice(ops)(v))
print(out)