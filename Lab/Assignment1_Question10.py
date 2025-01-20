def store_digits(number):
    digits = []
    for digit in str(abs(number)): 
        digits.append(int(digit))
    return digits

number = -2345789
digits_array = store_digits(number)
print(f"The digits of {number} are: {digits_array}")
