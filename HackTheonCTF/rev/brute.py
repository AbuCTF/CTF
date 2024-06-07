def variableA(param_1):
    import random
    import string
    sVar3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    pvVar4 = ''.join(random.choices(sVar3, k=param_1))
    return pvVar4

def variableB(param_1, param_2):
    pvVar2 = [ord(c) for c in param_1]
    return pvVar2

def variableC(param_1, param_2, param_3):
    xor_result = [x ^ y for x, y in zip(param_1, param_2)]
    return xor_result

def variableD(param_1, param_2):
    index_order = sorted(range(len(param_2)), key=lambda k: param_2[k])
    reordered_list = [param_1[i] for i in index_order]
    return reordered_list

def variableE(param_1):
    return ''.join([format(x, '02x') for x in param_1])

def decrypt(ciphertext, target_prefix):
    key_length = 5  # Assuming key length is 5

    # Brute-force decryption until the decrypted message starts with the target prefix
    while True:
        key = variableA(key_length)
        key_binary = variableB(key, len(key))
        ciphertext_binary = bytes.fromhex(ciphertext)

        xor_result = variableC(ciphertext_binary, key_binary, len(ciphertext_binary))

        sorted_key = sorted(key_binary)
        reordered_xor_result = variableD(xor_result, sorted_key)

        plaintext = variableE(reordered_xor_result)

        # Check if the decrypted message starts with the target prefix
        if plaintext.startswith(target_prefix):
            return key, plaintext

ciphertext = "446709213550020f3b28696533183206631e030743394d4531"
target_prefix = "BrU7e"
key, decrypted_message = decrypt(ciphertext, target_prefix)
print("Key:", key)
print("Decrypted message:", decrypted_message)
