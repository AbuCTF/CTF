import random

# Provided netcat outputs
outputs = [
    [157, 5, 116, 104, 22, 39, 209, 6, 215, 123, 220, 139, 1, 56, 116, 75, 65, 22, 64, 255, 71, 58, 248, 81, 221, 161, 62, 247, 199, 108, 126, 196, 189, 80, 183, 124],
    [15, 232, 222, 93, 79, 248, 181, 79, 16, 220, 252, 79, 180, 202, 182, 83, 118, 253, 147, 252, 140, 74, 129, 197, 127, 95, 160, 222, 235, 153, 35, 153, 94, 93, 87, 234],
    [194, 141, 15, 71, 71, 125, 205, 163, 49, 57, 16, 23, 146, 114, 13, 81, 89, 57, 140, 213, 205, 20, 162, 41, 234, 34, 76, 187, 199, 123, 178, 35, 221, 61, 247, 108],
    [169, 140, 33, 123, 72, 167, 81, 51, 249, 159, 243, 39, 114, 183, 37, 75, 54, 88, 180, 243, 167, 120, 137, 95, 129, 102, 255, 174, 5, 212, 173, 94, 189, 84, 78, 193]
]

# Function to reverse the flag given an encrypted output and a seed
def reverse_flag(encrypted_output, seed):
    random.seed(seed)
    flag = []
    for value in encrypted_output:
        random_value = random.randint(0, 255)
        original_char = value ^ random_value
        flag.append(chr(original_char))
    return ''.join(flag)

# Brute-force the seed
for output in outputs:
    for execution_time in range(0, 2**31):
        flag = reverse_flag(output, execution_time)
        if flag.startswith("AKASEC{"):
            print(f"Time: {execution_time} -> Flag: {flag}")
            # Stop if you find a readable flag, or print out multiple candidates
            break
