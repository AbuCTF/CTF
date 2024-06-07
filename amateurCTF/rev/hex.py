def reverse_hex_manipulation(hex_str):
    hex_bytes = bytearray.fromhex(hex_str)
    for idx in range(0, len(hex_bytes) - 2, 2):
        hex_bytes[idx], hex_bytes[idx + 1] = hex_bytes[idx + 1], hex_bytes[idx]
    for idx in range(1, len(hex_bytes) - 1, 2):
        hex_bytes[idx], hex_bytes[idx + 1] = hex_bytes[idx + 1], hex_bytes[idx]
    return hex_bytes.hex()

# Given output
output_hex = "ac4556b1d396bfe88aa93672398c9b4a4c3ac85ab9232fd1dc0916d7150f68edf4d3341b811945e29534d10d98e8f845e34ae59639d78ccf2f74f0a0281d70b70ac10e661f44b695df6b1fe2887ffc067d1eef578984e682996e3243cd7eaa5ffcf79f3a"

# Reverse hex manipulation
reversed_hex = reverse_hex_manipulation(output_hex)
print(reversed_hex)

