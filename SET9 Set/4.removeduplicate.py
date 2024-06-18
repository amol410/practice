# Write a program to remove duplicate elements from a list using a set.

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
my_list = [1, 2, 3, 2, 4, 3, 5, 1, 6]
print("Original list:", my_list)

unique_list = remove_duplicates(my_list)
print("List with duplicates removed:", unique_list)