def f(x):
    return 3 * x**2 - 1

def numerical_derivative_method_1(x, h):
    return (f(x + h) - f(x)) / h

def numerical_derivative_method_2(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x = 5  
h = 0.01 

method_1_result = numerical_derivative_method_1(x, h)
method_2_result = numerical_derivative_method_2(x, h)

print(f"Using Method 1, f'(x) at x = {x} is approximately: {method_1_result}")
print(f"Using Method 2, f'(x) at x = {x} is approximately: {method_2_result}")
