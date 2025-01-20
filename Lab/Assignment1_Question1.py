numbers = [2, 8, 10, 683, 45, 1, 996, 139, 190, 58, 730, 9, 800]

range_0_10 = []
range_10_100 = []
range_100_1000 = []

for number in numbers:
    if 0 <= number < 10:
        range_0_10.append(number)
    elif 10 <= number < 100:
        range_10_100.append(number)
    elif 100 <= number < 1000:
        range_100_1000.append(number)

print("Range [0, 10):", range_0_10)
print("Range [10, 100):", range_10_100)
print("Range [100, 1000]:", range_100_1000)
