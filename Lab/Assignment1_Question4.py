def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(20))
print(is_prime(23))

def sum_of_first_n_primes(n):
    prime_count = 0
    current_number = 2
    prime_sum = 0

    while prime_count < n:
        if is_prime(current_number):
            prime_sum += current_number
            prime_count += 1
        current_number += 1

    return prime_sum

result = sum_of_first_n_primes(20)
print(f"The sum of the first 20 prime numbers is: {result}")
