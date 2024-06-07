string = "Northwestorientairlinesflight305"
indices = [1, 2, 4, 7, 12, 20, 33]

for index in indices:
    if index >= len(string):
        print(f"Index {index} is out of range for the string.")
    else:
        print(f"Index {index}: {string[index]}")
