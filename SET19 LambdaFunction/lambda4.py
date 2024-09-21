# Write a lambda function to find the maximum value from a list of dictionaries.

# List of dictionaries
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]

# Using lambda to find the dictionary with the maximum 'age'
max_age = max(data, key=lambda x: x['age'])

# Output the dictionary with the maximum age
print("Dictionary with the maximum age:", max_age)


# output Dictionary with the maximum age: {'name': 'Bob', 'age': 30}
