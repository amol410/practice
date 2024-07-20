# Implement a program to find the difference between two sets.

def set_difference(set1, set2):
    return set1 - set2

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

difference1 = set_difference(set1, set2)
print("Difference of Set 1 - Set 2:", difference1)

difference2 = set_difference(set2, set1)
print("Difference of Set 2 - Set 1:", difference2)