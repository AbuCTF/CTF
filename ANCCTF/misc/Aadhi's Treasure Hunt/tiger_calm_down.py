import numpy as np
def liger_initializing(filename, dtype=np.float32):
    return np.fromfile(filename, dtype=dtype)
def Liger_calm_down(Muryo_signal, Kusho_bit_duration, Lions_samples_per_bit, Tiger_frequency0, Tiger_frequency1):
    num_bits = len(Muryo_signal) // Lions_samples_per_bit
    detected_bits = []

    t = np.linspace(0, Kusho_bit_duration, Lions_samples_per_bit, endpoint=False)
    
    for i in range(num_bits):
        start = i * Lions_samples_per_bit
        end = (i + 1) * Lions_samples_per_bit
        bit_segment = Muryo_signal[start:end]
        corr_0 = np.sum(bit_segment * np.sin(2 * np.pi * Tiger_frequency0 * t))
        corr_1 = np.sum(bit_segment * np.sin(2 * np.pi * Tiger_frequency1 * t))
        detected_bits.append(1 if corr_1 > corr_0 else 0)

    return ''.join(str(bit) for bit in detected_bits)
def Lion_to_tiger(binary_data):
    binary_data = binary_data.ljust((len(binary_data) + 7) // 8 * 8, '0')
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)
Muryo_signal = liger_initializing('moving_tiger.dat')

binary_data = Liger_calm_down(Muryo_signal, Kusho_bit_duration, Lions_samples_per_bit, Tiger_frequency0, Tiger_frequency1)

decoded_message = Lion_to_tiger(binary_data)
print("Decoded Message:", decoded_message)
