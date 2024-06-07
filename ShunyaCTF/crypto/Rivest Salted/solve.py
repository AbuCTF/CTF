import math

# Given parameters
c = 332390996033761218977578960091058900061139210257883065481008023465866203213646838419152404854307189904898248026722555965488045307811040694129009535565921
p = 95224848836921243754124073456831190902097637702298493988505946669357481749059
salted_q = 62480590829144807189161429469255353976579455660965599518063804867866301233320
salted_n = 5949704816946842021797594696485093255706996345339732550774644373410311670577880550185915164563052783086742129032939489765553432924892778486382904377417840
e = 65537

# XOR with 123456789
xor_value = 123456789
q = salted_q ^ xor_value

# Compute p
n = salted_n ^ xor_value
p = n // q

# Check if p and q are prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(num))
    for d in range(3, max_divisor + 1, 2):
        if num % d == 0:
            return False
    return True

if is_prime(p) and is_prime(q):
    print("p and q are prime.")
    # Decrypt the message
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    m = pow(c, d, n)
    flag = bytes.fromhex(hex(m)[2:]).decode('utf-8')
    print("Flag:", flag)
else:
    print("Invalid primes.")
