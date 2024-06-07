from Crypto.Random import random, get_random_bytes

BLOCK_SIZE = 16

with(open('wolverine.bmp', 'rb')) as f:
    wolverine = f.read()
with(open('flag.bmp', 'rb')) as f:
    flag = f.read()

w = open('wolverineOutput.bmp', 'wb')
f = open('flagOutput.bmp', 'wb')

f.write(flag[:55])
w.write(wolverine[:55])

for i in range(55, len(wolverine), BLOCK_SIZE):
    KEY = get_random_bytes(BLOCK_SIZE)
    w.write(bytes(a^b for a, b in zip(wolverine[i:i+BLOCK_SIZE], KEY)))
    f.write(bytes(a^b for a, b in zip(flag[i:i+BLOCK_SIZE], KEY)))
