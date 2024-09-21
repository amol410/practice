# Implement a program that uses a lambda function to find the smallest element in a list.

# Define a lambda function to find the smallest element in a list
find_smallest = lambda lst: min(lst)

# Example usage
numbers = [34, 11, 8, 73, 5, 22, 46]

# Use the lambda function to find the smallest number
smallest = find_smallest(numbers)

print(f"List: {numbers}")
print(f"The smallest number is: {smallest}")

# Test with different types of data
strings = ["apple", "banana", "cherry", "date"]
smallest_string = find_smallest(strings)

print(f"\nList of strings: {strings}")
print(f"The smallest string (alphabetically) is: {smallest_string}")

# Test with an empty list (will raise an exception)
try:
    find_smallest([])
except ValueError as e:
    print(f"\nError with empty list: {e}")