import base64

def reverse_func_1(unk_str1, unk_str):
    flag_len = len(unk_str1)
    unk_str_len = len(unk_str)

    unk_str0 = bytearray(unk_str1, 'utf-8')

    for i in range(flag_len):
        unk_str0[i] = unk_str0[i] ^ ord(unk_str[i % unk_str_len])

    return unk_str0.decode('utf-8')

def reverse_func_2(unk_str2):
    flag_len = len(unk_str2)
    unk_str0 = [''] * flag_len

    j = 0

    for i in range(0, flag_len , 4):
        unk_str0[i] = unk_str2[j]
        unk_str0[i + 1] = unk_str2[j + 1]
        j += 2

    for i in range(2, flag_len, 4):
        unk_str0[i] = unk_str2[j]
        unk_str0[i + 1] = unk_str2[j + 1]
        j += 2

    return ''.join(unk_str0)

def find_flag(unk_arr0):
    unk_str2 = ""
    for ascii_val in unk_arr0:
        unk_str2 += chr(ascii_val)

    unk_str1 = reverse_func_2(unk_str2)
    unk_str = "U2hhZG93MjAyNA=="
    unk_str = base64.b64decode(unk_str.encode('ascii')).decode('ascii')
    unk_str0 = reverse_func_1(unk_str1, unk_str)

    print("The flag is:", unk_str0)

if __name__ == "__main__":
    unk_arr0 = [32, 0, 27, 30, 84, 79, 86, 22, 97, 100, 63, 95, 60, 34, 1, 71, 0, 15, 81, 68, 6, 4, 91, 40, 87, 0, 9, 59, 81, 83, 102, 21]
    find_flag(unk_arr0)
