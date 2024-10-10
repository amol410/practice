# Implement a program that handles a KeyError exception for dictionary access.

def get_value_from_dict(my_dict, key):
    try:
        value = my_dict[key]
        print(f"Value for '{key}': {value}")
    except KeyError:
        print(f"Error: The key '{key}' does not exist in the dictionary.")

# Example usage
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

key = input("Enter the key you want to access: ")
get_value_from_dict(my_dict, key)
