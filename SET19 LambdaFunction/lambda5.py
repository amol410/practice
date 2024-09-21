# Create a program that defines a lambda function to calculate the average of a list of numbers.

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Lambda function to calculate the average
average = lambda nums: sum(nums) / len(nums) if nums else 0

# Calculate the average of the numbers
result = average(numbers)

# Output the average
print("Average of the list:", result)

# output Average of the list: 30.0
