# Create a program that defines a generator to produce a series of random integers.

import random

# Define the generator to yield random integers
def random_integer_generator(count, start=0, end=100):
    for _ in range(count):
        yield random.randint(start, end)

# Example usage
random_integers = random_integer_generator(5, 1, 10)

# Iterate through the generator and print random integers
for rand_int in random_integers:
    print(rand_int)
