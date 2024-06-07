import random
import time

flag = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]

for time_cycle in range(256):
    # Generate the same random bytes used during encryption
    random.seed(time_cycle)
    random_bytes = [random.getrandbits(8) for _ in range(len(flag))]

    # Decrypt the flag
    decrypted_flag = [byte ^ random_byte for byte, random_byte in zip(flag, random_bytes)]

    # Convert the decrypted flag to a string
    decrypted_flag_string = ''.join(chr(byte) for byte in decrypted_flag)

    print(f"Time Cycle: {time_cycle}, Decrypted Flag: {decrypted_flag_string}")
