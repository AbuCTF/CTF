def generator(g, x, p):
    return pow(g, x) % p

def decrypt(cipher, a, b):
    decrypted_text = ""
    for encrypted_char in cipher:
        key = generator(b, a, p)
        decrypted_char = chr((encrypted_char // key) // 311)
        decrypted_text += decrypted_char
    return decrypted_text

if __name__ == "__main__":
    cipher = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]
    a = 89
    b = 27
    p = 97  # Just an example, not used for decryption

    decrypted_text = decrypt(cipher, a, b)
    print(f"Decrypted message: {decrypted_text}")
