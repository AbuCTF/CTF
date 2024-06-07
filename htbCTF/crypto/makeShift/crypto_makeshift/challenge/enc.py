encrypted_flag = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
flag_length = len(encrypted_flag)
decrypted_flag = ''

# Reversing the process
for i in range(0, flag_length, 3):
    decrypted_flag += encrypted_flag[i+2]
    decrypted_flag += encrypted_flag[i]
    decrypted_flag += encrypted_flag[i+1]

# Reversing the final result
decrypted_flag = decrypted_flag[::-1]

print(decrypted_flag)

