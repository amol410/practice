# Implement a program to add a key-value pair to a dictionary.

def add_key_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# Example usage
my_dict = {"apple": 3, "banana": 5, "orange": 2}
print("Original dictionary:", my_dict)

new_key = "grape"
new_value = 7
updated_dict = add_key_value(my_dict, new_key, new_value)
print("Updated dictionary:", updated_dict)

existing_key = "banana"
new_value = 10
updated_dict = add_key_value(my_dict, existing_key, new_value)
print("Updated dictionary:", updated_dict)