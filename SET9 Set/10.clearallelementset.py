# clear all elements of a set

def clear_set(set1):
    set1.clear()
    return set1

# Example usage
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

cleared_set = clear_set(my_set)
print("Cleared Set:", cleared_set)

# Alternative approach using the clear() method directly
my_set = {1, 2, 3, 4, 5}
print