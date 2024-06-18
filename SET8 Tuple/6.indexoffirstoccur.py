# Implement a program to find the index of the 
# first occurrence of an element in a tuple.

# Example usage
my_tuple = (10, 20, 30, 40, 50, 60, 70, 40, 80, 90)
element_to_find = 40

# Initialize a variable to store the index
index = -1

# Iterate over each element in the tuple using enumerate()
for i, element in enumerate(my_tuple):
    if element == element_to_find:
        index = i
        break

if index != -1:
    print("Tuple:", my_tuple)
    print("Element to find:", element_to_find)
    print("Index of the first occurrence:", index)
else:
    print("Element not found in the tuple.")