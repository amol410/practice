# Write a program to remove a key from a dictionary.


# Create a dictionary
my_dict = {
    'apple': 2,
    'banana': 3,
    'orange': 1,
    'grape': 5
}

# Print the original dictionary
print("Original dictionary:", my_dict)

# Remove a key from the dictionary
key_to_remove = 'banana'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' has been removed.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

# Print the updated dictionary
print("Updated dictionary:", my_dict)