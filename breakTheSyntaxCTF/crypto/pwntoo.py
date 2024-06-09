from pwn import *
from Crypto.Util.number import inverse, long_to_bytes

def generate_p_candidates(msb, size=512):
    msb_len = len(msb)
    remaining_bits = size - msb_len
    base_p = int(msb, 2) << remaining_bits
    p_candidates = []
    for i in range(2**20):  # Adjust the range as needed
        candidate_p = base_p | i
        p_candidates.append(candidate_p)
    return p_candidates

def decrypt_rsa(ciphertext, n, e, p):
    q = n // p
    if n != p * q:
        return None  # p is not a valid factor
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(ciphertext, d, n)
    return long_to_bytes(m)

# Server details
host = 'leaky-prime.ch.bts.wh.edu.pl'
port = 1337

# Public exponent
e = 65537

while True:
    try:
        # Connect to the server
        conn = remote(host, port)

        # Receive data from the server
        ct = int(conn.recvline().strip().decode())
        n = int(conn.recvline().strip().decode())
        msb = conn.recvline().strip().decode()

        # Generate p candidates from the msb
        p_candidates = generate_p_candidates(msb)

        # Try to decrypt with each candidate
        for p in p_candidates:
            plaintext = decrypt_rsa(ct, n, e, p)
            if plaintext:
                print("Decrypted plaintext:", plaintext.decode())
                conn.close()
                exit(0)
        
        # Close the connection
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
