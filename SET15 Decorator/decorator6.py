# Implement a decorator that validates user input for a function.

from functools import wraps
from typing import Dict, Any, Callable

def validate_input(**validators: Dict[str, Callable[[Any], bool]]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Combine positional and keyword arguments
            sig = func.__signature__
            bound_args = sig.bind(*args, **kwargs)
            
            for param_name, validator in validators.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not validator(value):
                        raise ValueError(f"Invalid value for {param_name}: {value}")
            
            return func(*args, **kwargs)
        
        # Store the function signature for later use
        import inspect
        func.__signature__ = inspect.signature(func)
        
        return wrapper
    return decorator

# Example usage
@validate_input(
    age=lambda x: isinstance(x, int) and x >= 0,
    name=lambda x: isinstance(x, str) and len(x) > 0
)
def greet(name: str, age: int):
    """Greet a person with their name and age."""
    return f"Hello, {name}! You are {age} years old."

# Test the decorator
def main():
    try:
        print(greet("Alice", 30))  # Valid input
        print(greet("", 25))       # Invalid name
    except ValueError as e:
        print(f"Validation Error: {e}")
    
    try:
        print(greet("Bob", -5))    # Invalid age
    except ValueError as e:
        print(f"Validation Error: {e}")
    
    try:
        print(greet("Charlie", "thirty"))  # Invalid age type
    except ValueError as e:
        print(f"Validation Error: {e}")

if __name__ == "__main__":
    main()