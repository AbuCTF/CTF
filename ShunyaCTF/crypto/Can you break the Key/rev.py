def reverse_flag(encoded_flag):
    flag_unicode = []
    for i, c in enumerate(encoded_flag):
        flag_unicode.append(~((ord(c) - len(encoded_flag) * 6 - 15) // (-int(1 / (5**0.5) * ((1 + 5**0.5)**1 / 2 - (1 - 5**0.5)**1 / 2))) ^ i))
    flag_unicode.reverse()
    original_flag = ''.join([chr(c) for c in flag_unicode])
    return original_flag

encoded_flag = "ƃŰŶŉůļźŞŷŭŪƄŰŘŰŧŖŔŦĦŨĬƀźōşŋůĲňĳźĖőƃũťũŸŪĞ"
original_flag = reverse_flag(encoded_flag)
print(original_flag)

