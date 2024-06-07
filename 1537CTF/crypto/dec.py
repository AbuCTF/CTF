import itertools
import string

# Given ciphertext
ciphertext = "22ECCDB90936D5C2454A65A5BB4C120FB1C8567381C6DB368EB57D4C6BE8B6D8C860E5C6FAC1F48BF2291A5C9EA3C354715857E7"

# Convert hex string to bytes
ciphertext_bytes = bytes.fromhex(ciphertext)

# Function to decrypt the ciphertext with a given key
def decrypt(ciphertext_bytes, key):
    decrypted_bytes = bytes([c ^ k for c, k in zip(ciphertext_bytes, key)])
    return decrypted_bytes.decode('ascii', errors='ignore')

# Brute-force the key and decrypt the ciphertext
def brute_force_decrypt(ciphertext_bytes):
    flag_length = len(ciphertext_bytes)
    printable_chars = string.printable.encode()
    for key_candidate in itertools.product(printable_chars, repeat=flag_length):
        decrypted_text = decrypt(ciphertext_bytes, key_candidate)
        print(f"Trying key: {bytes(key_candidate).decode()}\nDecrypted text: {decrypted_text}\n")

# Brute-force decryption
brute_force_decrypt(ciphertext_bytes)
