def calculate_mean(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

def calculate_variance(arr):
    mean = calculate_mean(arr)
    variance_sum = 0
    for num in arr:
        variance_sum += (num - mean) ** 2
    return variance_sum / len(arr)

def calculate_standard_deviation(arr):
    variance = calculate_variance(arr)
    return variance ** 0.5

x = [1.2, 3.4, 5.6, 7.8, 2.1, 4.5, 6.7, 8.9, 10.0, 9.3]

mean = calculate_mean(x)
variance = calculate_variance(x)
std_dev = calculate_standard_deviation(x)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
