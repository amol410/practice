# Create a program that uses a lambda function to sort a list of tuples based on the second element.

# List of tuples
data = [(1, 5), (3, 2), (4, 8), (2, 1), (5, 7)]

# Sorting using a lambda function that targets the second element (index 1) of each tuple
sorted_data = sorted(data, key=lambda x: x[1])

# Output the sorted list
print("Sorted list based on the second element:", sorted_data)


# Output Sorted list based on the second element: [(2, 1), (3, 2), (1, 5), (5, 7), (4, 8)]
