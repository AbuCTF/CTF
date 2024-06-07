from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i^j for i, j in zip(a, cycle(b))]

f = open("enc.txt", "rb").read()
key = [72, 32, 110, 97, 105, 48, 54, 53]
print(key)

enc = bytearray(xor(f,key))

open('dec.png', 'wb').write(enc)