# Implement a program that uses a generator to generate prime numbers.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes():
    num = 2  # Start from the first prime number
    while True:
        if is_prime(num):
            yield num
        num += 1

# Using the generator to print the first 10 prime numbers
prime_gen = generate_primes()

for _ in range(10):
    print(next(prime_gen))
