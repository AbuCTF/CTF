def shanks_bsgs(g, B, p):
    # Step 1: Compute the value of m (ceiling of sqrt(p))
    m = int(p ** 0.5) + 1

    # Step 2: Precompute the values of g^j for j from 0 to m-1
    baby_steps = {}
    for j in range(m):
        baby_steps[pow(g, j, p)] = j

    # Step 3: Compute the value of g^(-m) mod p
    gm_inv = pow(g, -m, p)

    # Step 4: Compute B * g^(-m) for j from 0 to m-1 and check for a match with baby_steps
    for i in range(m):
        value = (B * pow(gm_inv, i, p)) % p
        if value in baby_steps:
            return i * m + baby_steps[value]

    # Step 5: If no match is found, return None
    return None

# Given values
p = 0xdd6cc28d
g = 0x83e21c05
B = 0xc4a21ba9

# Find the private key using Shank's Baby-step Giant-step algorithm
a = shanks_bsgs(g, B, p)
print("Private key (a):", a)
