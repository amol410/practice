# Create a Python decorator that measures the execution time of a function.

import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

# Example usage
@measure_time
def example_function(n):
    """An example function that does some work."""
    total = 0
    for i in range(n):
        total += i
    return total

# Test the decorator
result = example_function(1000000)
print(f"Result: {result}")