# Write a lambda function to find the sum of the squares of numbers in a list.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Lambda function to calculate the sum of squares
sum_of_squares = lambda nums: sum(map(lambda x: x ** 2, nums))

# Calculate the sum of squares
result = sum_of_squares(numbers)

# Output the result
print("Sum of squares:", result)

# Sum of squares: 55
