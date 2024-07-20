# Create a function that reverses a list in place.

def reverse_list(lst):
    # Get the length of the list
    length = len(lst)
    
    # Swap elements from both ends until the middle
    for i in range(length // 2):
        lst[i], lst[length - 1 - i] = lst[length - 1 - i], lst[i]

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

reverse_list(my_list)
print("Reversed List:", my_list)

#or


my_list = [1, 2, 3, 4, 5]
    # Get the length of the list
length = len(my_list)
    
    # Swap elements from both ends until the middle
list = my_list[::-1]

print(list)

# Example usage

