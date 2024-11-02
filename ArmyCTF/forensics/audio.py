import wave
import numpy as np

# Open the audio file
with wave.open('secret_comm.wav', 'rb') as audio_file:
    # Get basic information about the file
    n_channels = audio_file.getnchannels()
    sample_width = audio_file.getsampwidth()
    frame_rate = audio_file.getframerate()
    n_frames = audio_file.getnframes()

    print(f"Channels: {n_channels}")
    print(f"Sample Width: {sample_width} bytes")
    print(f"Frame Rate: {frame_rate} Hz")
    print(f"Total Frames: {n_frames}")

    # Read the frames from the audio file
    frames = audio_file.readframes(n_frames)

    # Convert the byte data to integers for easier analysis
    # Assuming the audio is 16-bit PCM, the frames are signed 16-bit integers
    audio_data = np.frombuffer(frames, dtype=np.int16)

    print(f"Total Audio Data Points: {len(audio_data)}")

    # Analyze the least significant bit (LSB) of each sample for hidden data
    hidden_bits = []

    for sample in audio_data:
        # Extract the least significant bit from the sample
        hidden_bits.append(sample & 1)

    # Convert the bits into bytes
    hidden_bytes = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    # Convert bits to characters (ASCII)
    hidden_message = ''.join([chr(int(''.join(map(str, byte)), 2)) for byte in hidden_bytes if len(byte) == 8])

    print("\nHidden Message (LSB):")
    print(hidden_message)
