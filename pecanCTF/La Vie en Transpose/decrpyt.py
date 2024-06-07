from detect_english import isEnglish
import transposition_encrypt

def brute_force_decrypt(encrypted_text_file, dictionary_file):
    with open(dictionary_file, 'r') as dictionary:
        english_words = set(dictionary.read().splitlines())

    with open(encrypted_text_file, 'r') as encrypted_file:
        encrypted_text = encrypted_file.read()

    for key in range(1, len(encrypted_text)):
        decrypted_text = transposition_encrypt.encrypt_message(key, encrypted_text)  # Use correct function name
        if isEnglish(decrypted_text):
            print(f"Decryption with key {key}:")
            print(decrypted_text)

# Paths to files
encrypted_text_file = 'encrypted-text.txt'
dictionary_file = 'dictionary.txt'

# Attempt decryption
brute_force_decrypt(encrypted_text_file, dictionary_file)


# Attempt decryption
brute_force_decrypt(encrypted_text_file, dictionary_file)