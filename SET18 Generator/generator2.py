# Create a generator that produces a Fibonacci sequence up to a specified number of terms.

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator to print the first 10 Fibonacci numbers
n_terms = 10
gen = fibonacci(n_terms)

for fib_num in gen:
    print(fib_num)
