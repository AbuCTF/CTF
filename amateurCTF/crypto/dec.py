from Crypto.Util.number import inverse

# Given public key components
N = 172391551927761576067659307357620721422739678820495774305873584621252712399496576196263035396006999836369799931266873378023097609967946749267124740589901094349829053978388042817025552765214268699484300142561454883219890142913389461801693414623922253012031301348707811702687094437054617108593289186399175149061
e = 65537

# Given ciphertext
c = 128185847052386409377183184214572579042527531775256727031562496105460578259228314918798269412725873626743107842431605023962700973103340370786679287012472752872015208333991822872782385473020628386447897357839507808287989016150724816091476582807745318701830009449343823207792128099226593723498556813015444306241

# Define function to decrypt RSA ciphertext
def rsa_decrypt(ciphertext, modulus, exponent):
    # Compute private key exponent
    d = inverse(exponent, modulus - 1)
    # Decrypt ciphertext
    plaintext = pow(ciphertext, d, modulus)
    return plaintext

# Decrypt the ciphertext
plaintext = rsa_decrypt(c, N, e)

# Print the decrypted plaintext
print("Decrypted plaintext:", plaintext)

# Convert the decrypted plaintext from integer to bytes
plaintext_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')

try:
    # Decode the bytes into a string of ASCII characters
    plaintext_ascii = plaintext_bytes.decode('ascii')
    print("Decrypted plaintext in ASCII:", plaintext_ascii)
except UnicodeDecodeError:
    print("Decryption result cannot be represented as ASCII.")
