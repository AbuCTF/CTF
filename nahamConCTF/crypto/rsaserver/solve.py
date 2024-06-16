from pwn import *
from Crypto.Util.number import long_to_bytes

# Connect to the remote server
conn = remote('challenge.nahamcon.com', 32545)

# Choose option 2 to view the encrypted flag
conn.sendlineafter(b'> ', b'2')

# Receive the response
response = conn.recvline().strip().split(b'> ')

# Check if the response contains the expected format
if len(response) < 2:
    print("Error: Unexpected response format.")
    conn.close()
    exit()

# Extract the RSA modulus (N) and the encrypted flag
n = int(response[1])
encrypted_flag = int(conn.recvline().strip().split(b'> ')[1])

# Function to decrypt the flag
def decrypt_flag(encrypted_flag, n):
    with open('flag.txt', 'r') as f:
        flag = f.read().strip()

    # Use brute force to find the decryption exponent (d)
    for e in range(500, 1001):
        try:
            d = pow(e, -1, (p - 1) * (q - 1))
            flag_int = pow(encrypted_flag, d, n)
            decrypted_flag = long_to_bytes(flag_int)
            if decrypted_flag.decode() == flag:
                return decrypted_flag
        except:
            continue

# Decrypt the flag
decrypted_flag = decrypt_flag(encrypted_flag, n)

# Print the flag
print("Decrypted flag:", decrypted_flag.decode())

# Close the connection
conn.close()
