# Implement a decorator that limits the execution of a function to a specified number of times.

from functools import wraps

def limit_calls(max_calls):
    def decorator(func):
        func.calls = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            if func.calls >= max_calls:
                raise ValueError(f"Function '{func.__name__}' has exceeded its call limit of {max_calls}")
            func.calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@limit_calls(max_calls=3)
def limited_function():
    """A function that can only be called a limited number of times."""
    print("This function is called.")

# Test the decorator
for i in range(4):
    try:
        limited_function()
    except ValueError as e:
        print(f"Error: {e}")