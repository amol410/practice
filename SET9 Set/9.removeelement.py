def remove_element(set1, element):
    if element in set1:
        set1.remove(element)
    return set1

# Example usage
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

element_to_remove = 3
updated_set = remove_element(my_set, element_to_remove)
print("Updated Set:", updated_set)