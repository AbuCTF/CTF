import hashlib

partial_hash = '228320bf01b40fdd2aa390f0a4'
given_hash = '07782a534d52dc001f75ed3b011dda5c'

# Iterate through all possible combinations of characters for the six unknown positions
for i in range(256):
    for j in range(256):
        for k in range(256):
            for l in range(256):
                for m in range(256):
                    for n in range(256):
                        unknown_chars = bytes([i, j, k, l, m, n]).hex()
                        full_string = partial_hash + unknown_chars
                        calculated_hash = hashlib.md5(bytes.fromhex(full_string)).hexdigest()
                        if calculated_hash == given_hash:
                            print(f"Solution found: MD5(X = {full_string}) = {given_hash}")

