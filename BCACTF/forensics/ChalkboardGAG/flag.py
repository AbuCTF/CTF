# Provided lines with differences
lines = [
    "I WILL NOT bE SNEAKY",
    "I WIcL NOT BE SNEAKY",
    "I WILL NOT BE SNEAKa",
    "I WcLL NOT BE SNEAKY",
    "I WILL NOT BE SNEAKt",
    "I WILL NOT Bf SNEAKY",
    "I {ILL NOT BE SNEAKY",
    "I WILL NOT BE SNEBKY",
    "I WILL NaT BE SNEAKY",
    "I WILL NOT BE SNRAKY",
    "I WILT NOT BE SNEAKY",
    "I WILL NOT _E SNEAKY",
    "I WILW NOT BE SNEAKY",
    "I WILL NOT BE SNEUKY",
    "I WI1L NOT BE SNEAKY",
    "I WILL NOT BE SNEADY",
    "I W_LL NOT BE SNEAKY",
    "I WILL NOT BE SBEAKY",
    "I WILL NOT B3 SNEAKY",
    "I _ILL NOT BE SNEAKY",
    "I WILL NOT BE SNEPKY",
    "I WILR NOT BE SNEAKY",
    "I WILL NOT BE SNuAKY",
    "I WIDL NOT BE SNEAKY",
    "I WILL NOT BE SNEAK}"
]

# Standard line for comparison
standard_line = "I WILL NOT BE SNEAKY"

# Extract differences
flag_characters = []
for line in lines:
    for i, (standard_char, char) in enumerate(zip(standard_line, line)):
        if standard_char != char:
            flag_characters.append(char)
            break

# Construct the flag
flag = ''.join(flag_characters)

# Print the flag
print(flag)
