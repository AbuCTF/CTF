from Crypto.Cipher import AES 
import binascii, sys
from Crypto.Util.Padding import pad

IV=b"****************"
def encrypt(plaintext, passphrase):
     # Example IV; should be random or derived
    aes = AES.new(passphrase.encode('utf-8'), AES.MODE_CBC, IV)
    ciphertext = aes.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return ciphertext

KEY = 'REDACTED' 
print("encrypted data:" + binascii.hexlify(encrypt(sys.argv[1], KEY)).decode('utf-8'))
