# Create a program that uses list comprehension to flatten a list of lists into a single list.

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# Example usage
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = flatten_list(nested_list)
print(flattened)