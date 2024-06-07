import base64
from string import punctuation

alphabet = list(punctuation)
data = "0CTF{}"
def main():
    key = ('')
    encrypted = ''.join([chr(ord(x) ^ int(key, 16)) for x in data])
    encrypted_data_base64 = base64.b64encode(encrypted.encode()).decode()
    
    print(encrypted_data_base64)

main()