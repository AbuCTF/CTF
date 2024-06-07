import random
import string

def encrypt_string(input_string, seed):
    random.seed(seed)
    
    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=len(input_string)))
    encrypted_string = ''
    for i in range(len(input_string)):
        encrypted_char = chr(ord(input_string[i]) ^ ord(key[i]))
        encrypted_string += encrypted_char
    return encrypted_string.encode().hex()


seed_value = ''
input_string = ""
encrypted = encrypt_string(input_string, seed_value)


