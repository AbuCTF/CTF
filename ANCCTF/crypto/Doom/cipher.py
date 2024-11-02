from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

# Given values
key = 'wvmxqmkm_qa_zmit'
plaintext = "passwords should be unguessable"
recovered_iv = binascii.unhexlify("bef07e1e00ccf75102f9d4b358f243cd")

# Convert key and plaintext to bytes
key_bytes = key.encode('utf-8')
plaintext_bytes = plaintext.encode('utf-8')

# Encrypt the plaintext using the recovered IV and the key
cipher = AES.new(key_bytes, AES.MODE_CBC, recovered_iv)
ciphertext = cipher.encrypt(pad(plaintext_bytes, AES.block_size))

# Print the full ciphertext in hex format
print("Constructed Ciphertext:", binascii.hexlify(ciphertext).decode('utf-8'))
