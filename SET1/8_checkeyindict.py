# check if key is in dictionary or not return true or false 
# Tried using function
def key_exists(dictionary, key):
    return key in dictionary

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(key_exists(my_dict, 'a'))  # Output: True
print(key_exists(my_dict, 'b'))  # Output: True
print(key_exists(my_dict, 'd'))  # Output: False


# tried using dict
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check if 'a' exists in the dictionary
if 'a' in my_dict:
    print(my_dict['a'])  # Output: 1
    print("yes available")
 



