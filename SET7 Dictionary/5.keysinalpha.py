# Create a function that returns the keys of a dictionary 
# in alphabetical order.

def get_sorted_keys(dictionary):
    return sorted(dictionary.keys())

# Example usage
my_dict = {"banana": 5, "apple": 3, "orange": 2, "grape": 7}
print("Original dictionary:", my_dict)

sorted_keys = get_sorted_keys(my_dict)
print("Keys in alphabetical order:", sorted_keys)