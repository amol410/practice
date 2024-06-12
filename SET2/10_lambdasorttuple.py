# Create a program that uses a lambda function to sort a list of tuples based on the second element.

# Define a list of tuples
my_list = [('apple', 5), ('banana', 2), ('orange', 8), ('grape', 3)]

# Sort the list based on the second element of each tuple using a lambda function
sorted_list = sorted(my_list, key=lambda x: x[1])

# Print the sorted list
print("Sorted list:", sorted_list)