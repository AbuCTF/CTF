import os

# Define the characters list
char = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

# Define the key
key = char[75] + char[78] + char[64] + char[67] + char[62] + char[69] + char[72] + char[75] + char[68]

def functionA(secret, inputB):
    with open(secret, 'rb') as secretFile:
        someValue = secretFile.read()
    byteOutput = bytes([OO0OO0O000OOOO000 ^ ord(inputB[OO0OOOOOOO0O00OO0 % len(inputB)]) for OO0OOOOOOO0O00OO0, OO0OO0O000OOOO000 in enumerate(someValue)])
    with open(secret, 'wb') as secretFile:
        secretFile.write(byteOutput)

# Provide the correct file path containing the encrypted message
secret_file_path = "secret"

# Decrypt the message
functionA(secret_file_path, key)

# Read the decrypted message
with open(secret_file_path, 'r') as decrypted_file:
    decrypted_message = decrypted_file.read()

print(decrypted_message)
