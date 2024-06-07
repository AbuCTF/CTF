def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(ciphertext):
    decrypted_message = ''
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if not ch.isalpha():
            decrypted_ch = ch
        else:
            chi = to_identity_map(ch)
            decrypted_ch = from_identity_map(chi - i)
        decrypted_message += decrypted_ch
    return decrypted_message

# Ciphertext to decrypt
ciphertext = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext)

print("Decrypted message:", decrypted_message)

