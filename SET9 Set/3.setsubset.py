# Implement a function to check if one set is a subset of another set.

def is_subset(set1, set2):
    return set1.issubset(set2)

# Example usage
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)
print("Is Set 1 a subset of Set 2?", is_subset(set1, set2))

print("\nSet 1:", set1)
print("Set 3:", set3)
print("Is Set 1 a subset of Set 3?", is_subset(set1, set3))