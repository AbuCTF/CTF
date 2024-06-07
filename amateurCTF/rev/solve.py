import random

# Set seed for reproducibility
seed_value = int('1665663c', 20)
random.seed(seed_value)

# Read the contents of the file (pretend we have 'output.txt' instead of 'flag.txt')
file_content = bytearray(open('output.txt', 'rb').read())

# Define a string with unclear purpose
weird_string = '\r''r''\\r'r'\\r\r'r'r''r''\\r'r'r\r'r'r\\r''r'r'r''r''\\r'r'\\r\r'r'r''r''\\r'r'rr\r''\r''r''r\\'r'\r''\r''r\\\r'r'r\r''\rr'

# Define a list of bytearrays with unclear purpose
bytearray_list = [
    b'bytearray1',
    b'bytearray2',
    b'bytearray3',
    b'bytearray4',
    b'bytearray5',
    b'bytearray6',
    b'bytearray7',
    b'bytearray8',
    b'bytearray9',
]

# Function to apply a series of transformations to a bytearray
def apply_transformations(arr, transformation_indices):
    for index in transformation_indices:
        arr = transformations[index](arr)
    return arr

# Function to perform a calculation based on the input bytearray and a string
def perform_calculation(byte_arr, string_to_use):
    # Convert string to an integer
    string_as_int = int(string_to_use.hex(), 17)
    # Perform calculation based on byte values in the input bytearray
    for byte_value in byte_arr:
        string_as_int += int(byte_value, 35)
    # Convert back to bytes and return
    return bytes.fromhex(hex(string_as_int)[2:])

# Perform some hex manipulation on a bytearray
def perform_hex_manipulation(byte_arr):
    for index in range(0, len(byte_arr) - 1, 2):
        byte_arr[index], byte_arr[index + 1] = byte_arr[index + 1], byte_arr[index]
    for index in range(1, len(byte_arr) - 1, 2):
        byte_arr[index], byte_arr[index + 1] = byte_arr[index + 1], byte_arr[index]
    return byte_arr

# Define transformations
transformation1 = lambda byte_arr: bytearray([value + 1 for value in byte_arr])
transformation2 = lambda byte_arr: bytearray([value - 1 for value in byte_arr])

# List of transformations
transformations = [perform_hex_manipulation, transformation1, transformation2]

# Choose random transformations to apply
random_transformations = [random.choice(range(len(transformations))) for _ in range(128)]

# Apply transformations
result = apply_transformations(file_content, random_transformations)

# Perform calculation
final_result = perform_calculation(result, weird_string)

# Print the hexadecimal representation of the resulting bytearray
print(final_result.hex())
