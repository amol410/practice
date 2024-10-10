# Write a program to find the sum of all elements in a list.

# Define the input list
numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the sum
total = 0

# Iterate over each element in the list
for num in numbers:
    # Add the current element to the total
    total += num

# Print the original list and the sum
print("List:", numbers)
print("Sum:", total)


#or 

# Define the input list
numbers = [10, 20, 30, 40, 50]

# Calculate the sum using the sum() function
total = sum(numbers)

# Print the original list and the sum
print("List:", numbers)
print("Sum:", total)


numb = [10, 20, 30, 40, 50]

total = 0

for i in numb:
    total += i  

print(total)    