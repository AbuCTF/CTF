from Crypto.Util.number import *
from flag import flag

n = getPrime(256) * getPrime(256)
e = 65537
print(n)
print(pow(bytes_to_long(flag), e, n))
