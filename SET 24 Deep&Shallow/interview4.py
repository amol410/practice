# remove 5 1st time then remove 2nd time and compare two

# Initial list
list1 = [1, 3, 5, 6, 7, 5]

# Step 1: Remove the first occurrence of 5
list1_first_removal = list1.copy()  # Copy the original list
list1_first_removal.remove(5)       # Remove the first occurrence of 5
num1 = int(''.join(map(str, list1_first_removal)))  # Convert list to a number
print(num1)  # Print the number (13675)
 
# Step 2: Remove the second occurrence of 5
list1_second_removal = list1.copy()  # Copy the original list again
list1_second_removal.reverse()       # Reverse the list to target the last occurrence
list1_second_removal.remove(5)       # Remove the first 5 (which is actually the last one in original order)
list1_second_removal.reverse()       # Reverse the list back to its original order
num2 = int(''.join(map(str, list1_second_removal)))  # Convert list to a number
print(num2)  # Print the number (13567)

# Step 3: Compare the two numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")
