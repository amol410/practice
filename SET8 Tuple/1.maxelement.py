# Write a program to find the maximum element in a tuple.

# Example usage
my_tuple = (10, 5, 8, 20, 3, 15)

# Find the maximum element in the tuple
max_element = my_tuple[0]  # Assume the first element is the maximum

for element in my_tuple:
    if element > max_element:
        max_element = element

print("Tuple:", my_tuple)
print("Maximum Element:", max_element)


# or

# Example usage
my_tuple = (10, 5, 8, 20, 3, 15)

# Find the maximum element using the max() function
max_element = max(my_tuple)

print("Tuple:", my_tuple)
print("Maximum Element:", max_element)