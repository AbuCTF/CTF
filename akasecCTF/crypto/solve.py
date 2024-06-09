from Crypto.Util.number import inverse, long_to_bytes

# Given values
n = 5113166966960118603250666870544315753374750136060769465485822149528706374700934720443689630473991177661169179462100732951725871457633686010946951736764639
c = 329402637167950119278220170950190680807120980712143610290182242567212843996710001488280098771626903975534140478814872389359418514658167263670496584963653
cor_m = 724154397787031699242933363312913323086319394176220093419616667612889538090840511507392245976984201647543870740055095781645802588721
e = 2

# Factor n to get p and q
from sympy.ntheory import factorint

factors = factorint(n)
p = list(factors.keys())[0]
q = list(factors.keys())[1]

# Calculate phi(n)
phi = (p - 1) * (q - 1)

# Calculate the private key d
d = inverse(e, phi)

# Decrypt the ciphertext
m = pow(c, d, n)

# We know cor_m = m - random_bits, so random_bits = m - cor_m
random_bits = m - cor_m

# Calculate the original message m
original_m = cor_m + random_bits

# Convert the long integer back to bytes
flag = long_to_bytes(original_m)

print("Flag:", flag.decode())
