def decrypt(data, seed, a, c, modulus):
    decrypted_data = bytearray()

    for byte in data:
        seed = (a * seed + c) % modulus
        decrypted_data.append(byte ^ seed)

    return decrypted_data

# Ciphertext
ciphertext = b'\x1aB]\x8fD\xa1r\x85+\xb0\xdc\x8a\xdfo\x9f\x9d\x11rlF3\x8c\xa1u\x8c\xa6*$\x15\x82\x9f\x1fw\x08D\x0c\x10[\xa3T\x8d!\xe3\x377\x88\x8eY\xa1Gs\x8e\x0b\x81{\x19\x14\x8e\x05\n\x8d\x17\x87lWk/\x90\xbb\x8d`\x90\xdf)\x90\x8e(\x90H\x8d\x9d=\x8f\x88Dg\x8b\x9f/\x8ec\x8b\x8e\x0c\x15\x8a\x9bK\x03m\x8bY\xc2\x89\x03(\x8e\x19\x8f\x86\x8a+?\x9b\\B\x9b\x8d\x0f\x91W\x8f\x81\x8d\n\x9b\xdbP'

# Brute-force decryption
for seed_guess in range(1, 256):
    for a_guess in range(1, 256):
        for c_guess in range(1, 256):
            for modulus_guess in range(1, 256):
                decrypted_data = decrypt(ciphertext, seed_guess, a_guess, c_guess, modulus_guess)

                # Output the guesses
                print("Seed guess:", seed_guess)
                print("A guess:", a_guess)
                print("C guess:", c_guess)
                print("Modulus guess:", modulus_guess)
                
                # Attempt to decode decrypted data
                try:
                    decrypted_str = decrypted_data.decode("utf-8", errors="replace")
                    print("Decrypted data:", decrypted_str)
                except UnicodeDecodeError:
                    print("Decoding failed. Decrypted data contains non-UTF-8 characters.")

                print()

