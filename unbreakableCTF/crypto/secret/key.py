# Define the characters list
char = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

# Extract characters for the key
key_characters = [char[75], char[78], char[64], char[67], char[62], char[69], char[72], char[75], char[68]]

# Join the characters to form the key
key = ''.join(key_characters)

# Print the key
print("The key is:", key)
