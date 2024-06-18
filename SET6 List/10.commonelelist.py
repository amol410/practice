#Write a program to find the common elements between two lists.

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find the common elements between list1 and list2
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common_elements)