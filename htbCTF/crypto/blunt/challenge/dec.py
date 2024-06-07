from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from hashlib import sha256

# Known parameters
p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'

# Calculate shared secret
C = pow(B, A, p)

# Derive key and IV
hash_obj = sha256()
hash_obj.update(long_to_bytes(C))
key = hash_obj.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'

def remove_padding(data):
    data = bytearray(data)  # Convert to bytearray to ensure indexing works
    padding_length = data[-1]
    if padding_length > len(data):
        raise ValueError("Invalid padding")
    return data[:-padding_length]

# Decrypt ciphertext
cipher = AES.new(key, AES.MODE_CBC, ciphertext[:16])  # IV is the first 16 bytes of ciphertext
plaintext_padded = cipher.decrypt(ciphertext[16:])
# plaintext = remove_padding(plaintext_padded)

print(plaintext_padded)
