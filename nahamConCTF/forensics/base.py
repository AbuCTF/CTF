import base64

# Define the input and output file paths
input_file = "theflag"
output_file = "decoded_theflag.txt"

# Read the Base64 encoded text from the input file
with open(input_file, "r") as f:
    encoded_text = f.read()

# Decode Base64
decoded_text = base64.b64decode(encoded_text)

# Write the decoded text to a new file
with open(output_file, "wb") as f:
    f.write(decoded_text)

print(f"Decoded text has been written to {output_file}.")
