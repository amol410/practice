# Create a generator that generates the powers of 2 (2^n) up to a specified limit.

# Define the generator to yield powers of 2 up to a given limit
def powers_of_two_generator(limit):
    n = 0
    while True:
        power_of_two = 2 ** n
        if power_of_two > limit:
            break
        yield power_of_two
        n += 1

# Example usage
limit = 1000
powers_of_two = powers_of_two_generator(limit)

# Iterate through the generator and print powers of 2
for power in powers_of_two:
    print(power)
