from Crypto.Cipher import AES

# Secret key
key = b'0123456789ABCDEF'

# Read ciphertext from file
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# Create AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt ciphertext
plaintext = cipher.decrypt(ciphertext)

# Remove padding
plaintext = plaintext.rstrip(b'\0')

# Print decrypted message
print("Decrypted message:", plaintext.decode('utf-8'))
