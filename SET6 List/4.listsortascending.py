# Write a function that checks if a list is sorted in ascending order.

def is_sorted(lst):
    # Iterate over the list, comparing each element with the next one
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    
    return True

# Example usage
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [10, 30, 20, 40, 50]

print("List 1:", numbers1)
print("Is sorted?", is_sorted(numbers1))

print("List 2:", numbers2)
print("Is sorted?", is_sorted(numbers2))