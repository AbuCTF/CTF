# Load the encrypted text from the file
from collections import Counter


with open('encrypted.txt', 'r') as file:
    encrypted_text = file.read()

# Function to perform frequency analysis on the encrypted text
def frequency_analysis(text):
    letter_count = Counter(text)
    total_letters = sum(letter_count.values())
    frequency_distribution = {letter: count / total_letters for letter, count in letter_count.items()}
    return frequency_distribution

# English letter frequencies (based on English language statistics)
english_frequencies = {
    'E': 0.127, 'T': 0.090, 'A': 0.081, 'O': 0.075, 'I': 0.069,
    'N': 0.067, 'S': 0.063, 'H': 0.060, 'R': 0.059, 'D': 0.042,
    'L': 0.040, 'C': 0.028, 'U': 0.028, 'M': 0.024, 'W': 0.023,
    'F': 0.022, 'G': 0.020, 'Y': 0.019, 'P': 0.019, 'B': 0.014,
    'V': 0.009, 'K': 0.008, 'J': 0.002, 'X': 0.002, 'Q': 0.001,
    'Z': 0.001
}

# Perform frequency analysis on the encrypted text
encrypted_frequencies = frequency_analysis(encrypted_text)

# Sort the encrypted frequencies in descending order
sorted_encrypted_frequencies = {k: v for k, v in sorted(encrypted_frequencies.items(), key=lambda item: item[1], reverse=True)}

# Create a mapping between encrypted letters and plaintext letters
letter_mapping = {}
for encrypted_letter, _ in sorted_encrypted_frequencies.items():
    english_letter = max(english_frequencies, key=lambda x: english_frequencies[x])
    letter_mapping[encrypted_letter] = english_letter
    del english_frequencies[english_letter]

# Decrypt the text using the letter mapping
decrypted_text = ''.join(letter_mapping.get(letter, letter) for letter in encrypted_text)

# Extract the flag from the decrypted text
flag = decrypted_text.split('\n')[-1].replace(' ', '_')

print("Decrypted text:")
print(decrypted_text)
print("\nFlag:")
print(flag)
