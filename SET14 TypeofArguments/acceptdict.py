# Implement a function that accepts a dictionary and extracts specific key-value pairs.

def extract_key_value_pairs(input_dict, keys):
    """
    Extracts specific key-value pairs from the input dictionary.

    Args:
        input_dict (dict): The dictionary to extract from.
        keys (list): The list of keys to extract.

    Returns:
        dict: A new dictionary containing only the specified key-value pairs.
    """
    # Using dictionary comprehension to filter key-value pairs
    return {key: input_dict[key] for key in keys if key in input_dict}

# Example usage:
input_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'email': 'alice@example.com'
}

# Extract specific keys
keys_to_extract = ['name', 'email']

# Call the function
extracted_dict = extract_key_value_pairs(input_dict, keys_to_extract)

print(extracted_dict)
# Output: {'name': 'Alice', 'email': 'alice@example.com'}
