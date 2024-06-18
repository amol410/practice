# Create a program to find the union of two sets.

def set_union(set1, set2):
    union = set()
    
    for element in set1:
        union.add(element)
    
    for element in set2:
        union.add(element)
    
    return union

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set_union(set1, set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union)


# trying other way
# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union)