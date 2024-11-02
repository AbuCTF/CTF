from Crypto.Cipher import AES
import binascii

# Given values
key = 'wvmxqmkm_qa_zmit'
ciphertext_hex = "69****************************f42b2a885a6e224f22d633f06b101546f4"
ciphertext = binascii.unhexlify(ciphertext_hex.replace('*', '0'))  # Replace '*' with '0' for decryption

# Extract the first block (16 bytes)
first_block = ciphertext[:16]

# Convert the key to bytes
key_bytes = key.encode('utf-8')

# Decrypt the first block using ECB mode
cipher_ecb = AES.new(key_bytes, AES.MODE_ECB)
decrypted_first_block = cipher_ecb.decrypt(first_block)

# Known plaintext
known_plaintext = "passwords should be unguessable"[:16]

# XOR the decrypted first block with the known plaintext to get the IV
iv = bytes([_a ^ _b for _a, _b in zip(decrypted_first_block, known_plaintext.encode('utf-8'))])

print("Recovered IV:", binascii.hexlify(iv).decode('utf-8'))
