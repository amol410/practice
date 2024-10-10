# Write a function that accepts a variable-length argument list and calculates their sum.

def calculate_sum(*args):
    """
    Calculates the sum of all given positional arguments.

    Parameters:
    *args: A variable-length tuple of numbers to be summed.

    Returns:
    float: The sum of all provided numbers. Returns 0 if no arguments are provided.
    """
    return sum(args)

# Example usage
print(calculate_sum(1, 2, 3, 4))          # Output: 10
print(calculate_sum(10, -5, 3.5))         # Output: 8.5
print(calculate_sum(100))                 # Output: 100
print(calculate_sum())                    # Output: 0
