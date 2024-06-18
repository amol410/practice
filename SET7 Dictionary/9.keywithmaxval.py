# Implement a function that returns the keys with 
# the maximum value in a dictionary.

def get_keys_with_max_value(dictionary):
    if len(dictionary) == 0:
        return []

    max_value = max(dictionary.values())
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    return max_keys

# Example usage
my_dict = {"apple": 3, "banana": 5, "orange": 2, "grape": 7, "kiwi": 7}
print("Original dictionary:", my_dict)

max_keys = get_keys_with_max_value(my_dict)
print("Keys with the maximum value:", max_keys)

empty_dict = {}
max_keys = get_keys_with_max_value(empty_dict)
print("Keys with the maximum value for empty dictionary:", max_keys)