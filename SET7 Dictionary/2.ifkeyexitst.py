# Write a function to check if a key exists in a dictionary.

def key_exists(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

# Example usage
my_dict = {"apple": 3, "banana": 5, "orange": 2}
print("Dictionary:", my_dict)

key_to_check = "banana"
if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

key_to_check = "grape"
if key_exists(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")