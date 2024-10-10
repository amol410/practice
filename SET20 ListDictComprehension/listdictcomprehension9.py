# Implement a dictionary comprehension to filter out key-value pairs with values greater than a specified number.

def filter_dict(input_dict, threshold):
    return {k: v for k, v in input_dict.items() if v <= threshold}

# Example usage
sample_dict = {'a': 1, 'b': 5, 'c': 3, 'd': 7, 'e': 2}
threshold = 4
result = filter_dict(sample_dict, threshold)
print(result)