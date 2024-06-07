#!/usr/bin/env python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from sage.all import matrix, Zmod

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = key.public_key()

# Extracting the modulus from the public key
n = public_key.public_numbers().n
print(f'n = {n}')
print()

pt = b'REDACTED'
pt = [int.from_bytes(pt[p:p + len(pt) // 4], byteorder='big') for p in range(0, len(pt), len(pt) // 4)]
g = matrix(Zmod(n), [[pt[0], pt[1]], [pt[2], pt[3]]])

def encrypt(g):
    return g ** public_key.public_numbers().e

c = encrypt(g)

for i in c:
    for j in i:
        print(j)
