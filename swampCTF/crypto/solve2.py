import random

def encrypt(data):
    # Generate random numbers for the LCG
    seed = random.randint(1, 256)
    a = random.randint(1, 256)
    c = random.randint(1, 256)
    modulus = random.randint(1, 256)

    # Encrypt the file contents with the LCG
    encrypted_data = bytearray()
    for byte in data:
        seed = (a * seed + c) % modulus
        encrypted_data.append(byte ^ seed)

    return encrypted_data, seed, a, c, modulus

def decrypt(data, seed, a, c, modulus):
    # Decrypt the file contents with the LCG
    decrypted_data = bytearray()
    for byte in data:
        seed = (a * seed + c) % modulus
        decrypted_data.append(byte ^ seed)

    return decrypted_data

# File to encrypt or decrypt
file_name = input("Please input the filename: ")

# Choose whether to encrypt or decrypt the file
choice = input("Enter 'encrypt' or 'decrypt' to perform the respective operation on the selected file: ")

# Open the file
with open(file_name, mode="rb") as f:
    data = f.read()

if choice == "encrypt":
    encrypted_data, seed, a, c, modulus = encrypt(data)

    print(f"Seed: {seed}")
    print(f"A: {a}")
    print(f"C: {c}")
    print(f"Modulus: {modulus}")

    # Write the encrypted file back to disk
    with open(f"{file_name}.enc", "wb") as binary_file:
        binary_file.write(encrypted_data)

elif choice == "decrypt":
    # Brute-force decryption
    for seed_guess in range(1, 256):
        for a_guess in range(1, 256):
            for c_guess in range(1, 256):
                for modulus_guess in range(1, 256):
                    decrypted_data = decrypt(data, seed_guess, a_guess, c_guess, modulus_guess)

                    # Check if the decryption produces a potential flag format
                    decrypted_str = decrypted_data.decode(errors="replace")
                    if decrypted_str.startswith("swampCTF{") and decrypted_str.endswith("}"):
                        print("Potential flag found:")
                        print("Seed:", seed_guess)
                        print("A:", a_guess)
                        print("C:", c_guess)
                        print("Modulus:", modulus_guess)
                        print("Decrypted data:", decrypted_str)

                        # Write the decrypted file back to disk
                        with open(f"{file_name}.dec", "wb") as binary_file:
                            binary_file.write(decrypted_data)
