from Crypto.Cipher import AES
from binascii import unhexlify


key = b'yougotthekeynjoy'
iv = bytes.fromhex('000102030405060708090a0b0c0d0e0f')
ciphertext = bytes.fromhex('69d5deb91a001151db5d98231574a51779acd1a84b9338a6750697c0af7e4591')


cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
plaintext_utf8 = plaintext.decode('utf-8')
print("Decrypted plaintext:", plaintext_utf8)

