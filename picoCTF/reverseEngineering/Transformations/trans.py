# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


# Encoded string
encoded_string = "楯呻㙢瑟湴㑟昸搲㘹絟"

# Initialize an empty string to store the decoded flag
decoded_flag = ""

# Iterate over each character in the encoded string
for i in range(0, len(encoded_string)):
    # Extract the Unicode code points of the two characters
    code_point1 = ord(encoded_string[i]) >> 8
    code_point2 = ord(encoded_string[i]) & 0xFF

    # Convert the code points to characters and append to the decoded flag
    decoded_flag += chr(code_point1) + chr(code_point2)

# Print the decoded flag
print(decoded_flag)
