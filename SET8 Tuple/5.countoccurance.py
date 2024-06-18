# Create a program that counts the occurrences of a specific element in a tuple.

# Example usage
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2)
element_to_count = 2

# Initialize a variable to store the count
count = 0

# Iterate over each element in the tuple
for element in my_tuple:
    if element == element_to_count:
        count += 1

print("Tuple:", my_tuple)
print("Element to count:", element_to_count)
print("Count:", count)


# or 

# Example usage
my_tuple = (1, 2, 3, 2, 4, 2, 5, 2)
element_to_count = 2

# Count the occurrences using the count() method
count = my_tuple.count(element_to_count)

print("Tuple:", my_tuple)
print("Element to count:", element_to_count)
print("Count:", count)