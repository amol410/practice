# Create a program that defines a decorator to print the output of a function in a specific format.

# Define a decorator to format the output of a function
def format_output(format_string):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the original function and get the result
            result = func(*args, **kwargs)
            
            # Return the formatted result
            return format_string.format(result)
        
        return wrapper
    return decorator

# Example usage
@format_output("The result is: {}")
def add(a, b):
    return a + b

@format_output("Your output: {}")
def multiply(a, b):
    return a * b

# Test the functions
print(add(10, 20))         # The result is: 30
print(multiply(5, 6))      # Your output: 30
