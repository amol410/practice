# Write a Python program to merge two lists.

# Example usage
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

# Merge the lists using the + operator
merged_list = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)


#or 

# Example usage
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

# Merge the lists and sort the result
merged_list = sorted(list1 + list2)

print("List 1:", list1)
print("List 2:", list2)
print("Merged and Sorted List:", merged_list)