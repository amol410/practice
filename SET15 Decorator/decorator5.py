# Write a decorator that caches the results of a function and returns cached values for repeated input arguments.

from functools import wraps

def cache_result(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from the function arguments
        key = str(args) + str(kwargs)
        
        if key not in cache:
            # If the result isn't cached, compute and store it
            result = func(*args, **kwargs)
            cache[key] = result
            print(f"Computed result for {func.__name__}{args}: {result}")
        else:
            print(f"Using cached result for {func.__name__}{args}")
        
        return cache[key]
    return wrapper

# Example usage
@cache_result
def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the decorator
def main():
    print(fibonacci(10))  # This will compute and cache results
    print(fibonacci(10))  # This will use the cached result
    print(fibonacci(5))   # This will use some cached results and compute others
    print(fibonacci(5))   # This will use the cached result

if __name__ == "__main__":
    main()