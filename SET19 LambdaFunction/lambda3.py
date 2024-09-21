# Implement a lambda function to filter out even numbers from a list.

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a lambda function to filter out even numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Output the filtered list
print("List of odd numbers:", odd_numbers)


# output List of odd numbers: [1, 3, 5, 7, 9]
