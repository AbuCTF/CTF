import numpy as np
def liger_initializing(filename, dtype=np.float32):
    return np.fromfile(filename, dtype=dtype)
def liger_Roar(Muryo_signal, Kusho_bit_duration, Lions_samples_per_bit, tigers_amplitude_threshold):
    num_bits = len(Muryo_signal) // Lions_samples_per_bit 
    detected_bits = []
    for i in range(num_bits):
        start = i * Lions_samples_per_bit
        end = (i + 1) * Lions_samples_per_bit
        symbol_segment = Muryo_signal[start:end]
        avg_amplitude = np.mean(np.abs(symbol_segment))
        detected_bits.append('1' if avg_amplitude > tigers_amplitude_threshold else '0')

    binary_data = ''.join(detected_bits)
    return binary_data
def Lion_to_Tiger(binary_data):
    padding = len(binary_data) % 8
    if padding != 0:
        binary_data += '0' * (8 - padding)
    byte_array = bytearray()
    for i in range(0, len(binary_data), 8):
        byte_array.append(int(binary_data[i:i+8], 2))
    try:
        message = byte_array.decode('ascii')
    except UnicodeDecodeError:
        message = "Decoding error. Binary data might be incorrect."
    return message
Muryo_signal = liger_initializing('moving_lion.dat')
binary_data = liger_Roar(Muryo_signal, Kusho_bit_duration, Lions_samples_per_bit, tigers_amplitude_threshold)

decoded_message =Lion_to_Tiger(binary_data)
print("Decoded Message:", decoded_message)
