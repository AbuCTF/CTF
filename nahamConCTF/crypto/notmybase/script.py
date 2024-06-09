import binascii

# Your BinHex data, but it appears it might be Base64 encoded data
binhex_data = "F#S<YRXdP0Fd=,%J4c$Ph7XV(gF/*]%C4B<qlH+%3xGHo)\\"

# Correcting the input if it's Base64 instead
binhex_data = binhex_data.replace('#', '+').replace('S<', '/').replace('=', '')

try:
    decoded_data = binascii.a2b_base64(binhex_data)
    print(decoded_data.decode('utf-8', errors='ignore'))  # Assuming the data is text
except binascii.Error as e:
    print("Error decoding:", e)
