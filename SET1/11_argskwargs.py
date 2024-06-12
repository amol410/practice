# Write a Python function that demonstrates the use of *args and **kwargs in function definitions.

def example_function(*args, **kwargs):
    print("Arguments passed as *args:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments passed as **kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
example_function(1, 2, 3, name="Alice", age=25, city="New York")