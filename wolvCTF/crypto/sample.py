import random, time, sys

rand = random.getrandbits(8)
print(rand)

flag = [189, 24, 103, 164, 36, 233, 227, 172, 244, 213, 61, 62, 84, 124, 242, 100, 22, 94, 108, 230, 24, 190, 23, 228, 24]
print("Flag:", flag)
time_cycle = int(time.time()) % 256
print("Time Cycle:", time_cycle)

flagString = ''.join(chr(i) for i in flag)
encodeFlag = flagString.encode('utf-8')
print("Encoded Flag:", encodeFlag)

for i in range(len(encodeFlag)):
    random.seed(i + time_cycle)
    decrypted_byte = ord(flag[i]) ^ random.getrandbits(8)
    flag.append(decrypted_byte)

print(decrypted_byte)