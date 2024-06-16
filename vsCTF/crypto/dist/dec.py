import random

# Seed the random number generator with the same seed
random.seed(1337)

# Define the same operations as in the encryption script
ops = [
    lambda x: x-3,
    lambda x: x+3,
    lambda x: x // 3,  # Integer division to reverse multiplication by 3
    lambda x: x ^ 3    # XOR with 3 to reverse XOR operation
]

# Encrypted values from out.txt
encrypted_values = [
    354, 112, 297, 119, 306, 369, 111, 108, 333, 110, 112, 92, 111, 315,
    104, 102, 285, 102, 303, 100, 112, 94, 111, 285, 97, 351, 113, 98,
    108, 118, 109, 119, 98, 94, 51, 56, 159, 50, 53, 153, 100, 144, 98,
    51, 53, 303, 99, 52, 49, 128
]

# Store decrypted flag bytes
decrypted_flag = []

# Decrypt each encrypted value
for v in encrypted_values:
    # Iterate through each operation and check if it decrypts correctly
    for op in ops:
        try:
            decrypted_value = op(v)
            # Check if the decrypted value is in the valid range of ASCII values
            if decrypted_value >= 0 and decrypted_value <= 255:
                decrypted_flag.append(decrypted_value)
                break
        except:
            continue

# Convert decrypted ASCII values to characters
flag = bytes(decrypted_flag).decode('utf-8')

print("Decrypted flag:", flag)
