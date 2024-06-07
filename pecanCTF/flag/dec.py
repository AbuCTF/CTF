# Open the image file in binary mode
with open('pecan.jpg', 'rb') as file:
    # Read the raw bytes from the image file
    raw_bytes = file.read()

# Convert each byte to its ASCII number and decode it
decoded_string = ''
for byte in raw_bytes:
    try:
        ascii_number = ord(byte)
        decoded_string += chr(ascii_number)
    except:
        pass
# Print the decoded string
print(decoded_string)
