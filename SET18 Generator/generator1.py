# Write a Python generator that generates a sequence of even numbers.

def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

# Using the generator to print the first 10 even numbers
gen = even_numbers()

for _ in range(10):
    print(next(gen))
