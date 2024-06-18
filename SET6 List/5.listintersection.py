# Create a program to find the intersection of two lists.

def find_intersection(list1, list2):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of the sets
    intersection = set1.intersection(set2)
    
    # Convert the intersection set back to a list
    result = list(intersection)
    
    return result

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = find_intersection(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Intersection:", intersection)