import base64

encrypted_data_base64 = "1JjVq9W81a7Vk9Sd1YfVhdWN1J/VgdWF1JvVm9W31YHUn9W31YbVjdSb1YzUndW31ZzUmNW31YrUm9W31YvUmNWF1ZjVhNSb1ZDVlQ=="

encrypted_data = base64.b64decode(encrypted_data_base64).decode()

def decrypt(encrypted_data, key):
    key = key * (len(encrypted_data) // len(key)) + key[:len(encrypted_data) % len(key)]
    decrypted = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(encrypted_data, key)])
    return decrypted

def find_key(plaintext, ciphertext):
    key = ''
    for p, c in zip(plaintext, ciphertext):
        key += chr(ord(p) ^ ord(c))
    return key

def main():
    plaintext = "0CTF"
    key = find_key(plaintext, encrypted_data)
    decrypted_data = decrypt(encrypted_data, key)
    print(decrypted_data)

main()
