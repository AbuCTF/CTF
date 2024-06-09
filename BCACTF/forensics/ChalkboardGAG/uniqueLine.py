from collections import Counter

# Read the file
with open('chalkboardgag.txt', 'r') as file:
    lines = file.readlines()

# Count occurrences of each line
line_counts = Counter(lines)

# Identify lines that are unique (occur only once)
unique_lines = [line for line, count in line_counts.items() if count == 1]

# Print unique lines
for line in unique_lines:
    print(line.strip())
