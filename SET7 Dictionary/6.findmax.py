# Implement a program to find the maximum value in a dictionary's values.

def find_max_value(dictionary):
    if len(dictionary) == 0:
        return None
    return max(dictionary.values())

# Example usage
my_dict = {"apple": 3, "banana": 5, "orange": 2, "grape": 7}
print("Original dictionary:", my_dict)

max_value = find_max_value(my_dict)
print("Maximum value:", max_value)

empty_dict = {}
max_value = find_max_value(empty_dict)
print("Maximum value for empty dictionary:", max_value)