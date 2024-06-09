def main():
    print("Decrypting...")
    
    # Encrypted text
    encrypted = '🙚🙒🙌🙭😌🙧🙬🙻🙠🙓😣🙯🙖🙺🙠🙖😡🙃🙭🙿🙩🙟😯🙮🙬🙸🙻🙦😨🙩🙽🙉🙻🙑😯🙥🙻🙳🙐🙓😿🙯🙽🙉🙣🙐😡🙹🙖🙤🙪🙞😿🙰🙨🙤🙐🙕😯🙨🙽🙳🙽🙊😷'

    # Known prefix and suffix of the flag
    prefix = 'SDCTF{'
    suffix = '}'

    # Brute force the key
    for i in range(len(prefix)):
        for j in range(len(suffix)):
            key = chr(ord(prefix[i]) ^ ord(encrypted[i])) + chr(ord(suffix[j]) ^ ord(encrypted[-len(suffix) + j]))
            plaintext = ''.join([chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted)])
            if plaintext.startswith('SDCTF{') and plaintext.endswith('}'):
                print("Potential flag found with key:", key)
                print("Decrypted text:", plaintext)
                return

main()
