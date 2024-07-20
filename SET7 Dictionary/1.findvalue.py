# Create a program to find the value 
# associated with a specific key in a dictionary.

def find_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

# Example usage
my_dict = {"apple": 3, "banana": 5, "orange": 2}
print("Dictionary:", my_dict)

key_to_find = "banana"
value = find_value(my_dict, key_to_find)
if value is not None:
    print(f"The value associated with the key '{key_to_find}' is: {value}")
else:
    print(f"The key '{key_to_find}' does not exist in the dictionary.")

key_to_find = "grape"
value = find_value(my_dict, key_to_find)
if value is not None:
    print(f"The value associated with the key '{key_to_find}' is: {value}")
else:
    print(f"The key '{key_to_find}' does not exist in the dictionary.")