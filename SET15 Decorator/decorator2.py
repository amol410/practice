# Write a decorator that logs the function name and its arguments before execution.

import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        return func(*args, **kwargs)
    return wrapper

# Example usage
@log_function_call
def greet(name, greeting="Hello"):
    """A simple greeting function."""
    return f"{greeting}, {name}!"

# Test the decorator
result = greet("Alice")
print(result)

result = greet("Bob", greeting="Hi")
print(result)