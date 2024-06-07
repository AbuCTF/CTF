from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = b''

cipher = AES.new(key, AES.MODE_ECB)
message = b""
padded_message = message.ljust((len(message) + 15) // 16 * 16, b'\0')
ciphertext = cipher.encrypt(padded_message)

with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)


