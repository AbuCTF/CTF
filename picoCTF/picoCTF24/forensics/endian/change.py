def reverse_jpeg(file_path, output_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    reversed_data = bytearray(data)

    for i in range(0, len(data), 4):
        chunk = reversed_data[i:i+4]
        chunk.reverse()
        reversed_data[i:i+4] = chunk

    with open(output_path, 'wb') as f:
        f.write(reversed_data)

# Usage
input_file = "input.jpeg"
output_file = "output_reversed.jpeg"
reverse_jpeg(input_file, output_file)
print("JPEG file reversed every 4 bytes and saved as", output_file)
