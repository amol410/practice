# Write a Python program to find the symmetric difference between two sets.

def symmetric_difference(set1, set2):
    return set1 ^ set2

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

sym_diff = symmetric_difference(set1, set2)
print("Symmetric Difference:", sym_diff)