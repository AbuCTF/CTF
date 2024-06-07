from Crypto.Cipher import AES
import time

# Define the key generation function
def get_random_number():
    global seed 
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed

# Given ciphertext
ciphertext = "4bf05ac4a3e3d313821d81509f9c63994eeab466a3f3bb61d4ec26d0b5280bae1e5e05b995952411d6a3a146b8a323bd07aa6eae98c9426e69985fc75302924aeeadff9f6c675c7f739e054fd5b53bde24ad7962c3b8ca28cf652343f3bce2fb58ca4a3592480dcf1163bb445ff113cf"

# Key generation
seed = int(time.time() * 1000) % (10 ** 6)
key = b''
for i in range(8):
    key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')

# Decrypt function
# Decrypt function
def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(bytes.fromhex(ciphertext))
    # Remove padding
    padding_length = decrypted_message[-1]
    decrypted_message = decrypted_message[:-padding_length]
    return decrypted_message


# Decrypt the message
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
