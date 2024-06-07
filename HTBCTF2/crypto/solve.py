import binascii

# Function to perform RSA decryption
def rsa_decrypt(ciphertext, n, d):
    # Convert the ciphertext from hexadecimal to integer
    c = int(ciphertext, 16)
    
    # Perform decryption: plaintext = ciphertext^d mod n
    plaintext = pow(c, d, n)
    
    # Convert the plaintext from integer to bytes and then to a string
    decrypted_message = binascii.unhexlify(hex(plaintext)[2:]).decode()
    
    return decrypted_message

# Given values
ciphertext = "564ac7122cf386adfdde2d119f06b8609211e2a131f919b184d12bbb00cd606c"
n = 5438
d = 24139

# Decrypt the ciphertext
decrypted_message = rsa_decrypt(ciphertext, n, d)

# Print the decrypted message
print("Decrypted Message:", decrypted_message)
