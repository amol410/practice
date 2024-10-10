# Create a function to add an element to a set.
# set me add, remove & clear() use kiya jata h

def add_element(set1, element):
    set1.add(element)
    return set1

# Example usage
my_set = {1, 2, 3, 4}
print("Original Set:", my_set)

new_element = 5
updated_set = add_element(my_set, new_element)
print("Updated Set:", updated_set)