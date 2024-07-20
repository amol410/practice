# Create a program that checks if two sets are disjoint.

def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

# Example usage
set1 = {1, 2, 3, 4}
set2 = {6, 7, 8}
set3 = {3, 4, 8, 9}

print("Set 1:", set1)
print("Set 2:", set2)
print("Are Set 1 and Set 2 disjoint?", are_disjoint(set1, set2))

print("\nSet 1:", set1)
print("Set 3:", set3)
print("Are Set 1 and Set 3 disjoint?", are_disjoint(set1, set3))