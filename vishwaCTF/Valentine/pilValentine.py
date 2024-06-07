from PIL import Image
from itertools import cycle

def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, cycle(b)))

# Read the encrypted file
enc_data = open("enc.txt", "rb").read()

# Extract the XOR key from the encrypted data
key = [72, 38, 110, 97, 105, 48, 54, 53]
print(key)
# Decrypt the data
dec_data = xor(enc_data[8:], key)

# Write the decrypted data to a file
open("dec.png", "wb").write(dec_data)

print("Image decrypted and saved as 'dec.png'.")