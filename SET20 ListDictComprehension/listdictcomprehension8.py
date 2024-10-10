# Write a list comprehension to calculate the sum of all prime numbers up to 50.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = sum([num for num in range(2, 51) if is_prime(num)])
print(prime_sum)