from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

ciphertext_hex = "77efbfbdefbfbdefbfbd25efbfbd740d0aefbfbd6fefbfbd4fefbfbd2cefbfbd5d6defbfbd6c02237fefbfbdefbfbd2defbfbd41efbfbdefbfbdd383efbfbd2847efbfbd32efbfbdefbfbdefbfbd1defbfbdefbfbd0d0aefbfbd6e3e77efbfbd"

# Convert hexadecimal string to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)

# Function to decrypt ciphertext using a key and check if it starts with '0CTF'
def decrypt_and_check(key):
    try:
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        # Remove padding
        decrypted = decrypted.rstrip(b'\0')
        # Check if decrypted plaintext starts with '0CTF'
        if decrypted.startswith(b'0CTF'):
            return True, decrypted
    except Exception as e:
        pass
    return False, None

# Generate all possible 8-byte keys
def generate_keys():
    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    for m in range(256):
                        for n in range(256):
                            for o in range(256):
                                for p in range(256):
                                    key = bytes([i, j, k, l, m, n, o, p])
                                    yield key

# Brute force attack
for key in generate_keys():
    found, decrypted = decrypt_and_check(key)
    if found:
        print("Key found:", key)
        print("Decrypted plaintext:", decrypted)
        break
