# Create a program to merge two dictionaries.

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage
dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"grape": 7, "kiwi": 4, "apple": 6}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)

# or dict1.update(dict2)