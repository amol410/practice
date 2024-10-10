# Write a Python function that accepts a list and unpacks it into individual arguments.

def unpack_list(input_list):
    # Unpacking the list into individual arguments
    def inner_function(*args):
        for arg in args:
            print(arg)
    
    # Calling the inner function with unpacked list elements
    inner_function(*input_list)

# Example usage
sample_list = [1, 2, 3, 4, 5]
unpack_list(sample_list)
