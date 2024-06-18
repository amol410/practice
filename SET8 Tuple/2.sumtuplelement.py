# Create a program to find the sum of elements in a tuple.

# Example usage
my_tuple = (10, 5, 8, 20, 3, 15)

# Initialize a variable to store the sum
sum_of_elements = 0

# Iterate over each element in the tuple
for element in my_tuple:
    sum_of_elements += element

print("Tuple:", my_tuple)
print("Sum of Elements:", sum_of_elements)


# or

# Example usage
my_tuple = (10, 5, 8, 20, 3, 15)

# Calculate the sum of elements using the sum() function
sum_of_elements = sum(my_tuple)

print("Tuple:", my_tuple)
print("Sum of Elements:", sum_of_elements)