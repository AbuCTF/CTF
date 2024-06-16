import os
from pwn import xor

# Replace this with the extracted key from the PCAP file
key = b'leet hacker broken'

def decrypt(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    decrypted = xor(data, key)
    return decrypted

def decrypt_all_files():
    # Update the file paths according to your directory structure
    file_paths = [
        'ecorp.png',
        'id_rsa',
        'id_rsa.pub',
        'resources.zip',
        'Welcome aboard.pdf'
    ]
    
    for filepath in file_paths:
        decrypted_data = decrypt(filepath, key)
        decrypted_filename = 'decrypted_' + os.path.basename(filepath)
        with open(decrypted_filename, 'wb') as f:
            f.write(decrypted_data)
        print(f'Decrypted {filepath} to {decrypted_filename}')

decrypt_all_files()
