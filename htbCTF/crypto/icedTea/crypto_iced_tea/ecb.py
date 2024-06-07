from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from Crypto.Util.Padding import unpad
from enum import Enum

class Cipher:
    def __init__(self, key):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
    
    def decrypt(self, ct):
        blocks = [ct[i:i+self.BLOCK_SIZE//8] for i in range(0, len(ct), self.BLOCK_SIZE//8)]
        
        pt = b''
        for ct_block in blocks:
            pt += self.decrypt_block(ct_block)
        return pt

    def decrypt_block(self, ct_block):
        c = b2l(ct_block)
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        m0 = c >> (self.BLOCK_SIZE // 2)
        m1 = c & ((1 << (self.BLOCK_SIZE // 2)) - 1)

        s = self.DELTA * 32
        for i in range(32):
            m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
            m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            s -= self.DELTA
        
        return l2b((m0 << (self.BLOCK_SIZE // 2)) + m1)

# Given components
KEY = bytes.fromhex("850c1413787c389e0b34437a6828a1b2")
ct = bytes.fromhex("b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843")

# Decrypt the ciphertext
cipher = Cipher(KEY)
pt = cipher.decrypt(ct)

# Unpad the plaintext
unpadded_pt = unpad(pt, cipher.BLOCK_SIZE // 8)

print("Decrypted plaintext (ECB):", unpadded_pt.decode())
