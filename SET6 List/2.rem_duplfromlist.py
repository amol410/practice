# Create a program to remove duplicate elements from a list.

# Define the input list
numbers = [10, 20, 30, 40, 20, 50, 30, 60, 40]

# Create a new empty list to store the unique elements
unique_numbers = []

# Iterate over each element in the original list
for num in numbers:
    # Check if the current element is not already in the unique_numbers list
    if num not in unique_numbers:
        # If it's not present, append it to the unique_numbers list
        unique_numbers.append(num)

# Print the original list and the list with unique elements
print("Original list:", numbers)
print("List with unique elements:", unique_numbers)


# or 

# Define the input list
numbers = [10, 20, 30, 40, 20, 50, 30, 60, 40]

# Convert the list to a set to remove duplicates
unique_numbers = list(set(numbers))

# Print the original list and the list with unique elements
print("Original list:", numbers)
print("List with unique elements:", unique_numbers)