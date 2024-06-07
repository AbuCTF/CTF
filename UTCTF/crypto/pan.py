def luhn_check(number):
    number = [int(x) for x in str(number)]
    total = 0
    length = len(number)
    parity = length % 2

    for i, digit in enumerate(number):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

# Example usage:
pan = "89980142232765"
is_valid = luhn_check(pan)
print("PAN is valid." if is_valid else "PAN is not valid.")
