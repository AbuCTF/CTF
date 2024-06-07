import string
import random

def decrypt_string(encrypted_string, seed):
    random.seed(seed)
    
    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=len(encrypted_string) // 2))
    
    decrypted_string = ''
    for i in range(len(encrypted_string) // 2):
        decrypted_char = chr(int(encrypted_string[i*2:i*2+2], 16) ^ ord(key[i % len(key)]))
        decrypted_string += decrypted_char
    return decrypted_string

seed_value = "202242269"
encrypted_string = "5e04610a22042638723c571e1a5436142764061f39176b4414204636251072220a35583a60234d2d28082b"
plaintext = decrypt_string(encrypted_string, seed_value)
print("Plaintext:", plaintext)
