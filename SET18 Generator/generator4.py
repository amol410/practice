# Write a generator that yields a sequence of squares of numbers.

# Define the generator to yield squares of numbers
def square_generator(limit):
    for i in range(1, limit + 1):
        yield i * i

# Example usage
squares = square_generator(5)

# Iterate through the generator
for square in squares:
    print(square)
