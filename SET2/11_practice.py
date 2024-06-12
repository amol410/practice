#4 Create a program to find the union of two sets.

def set_union(set1, set2):
    union = set()

    for element in set1:
        union.add(element)

    for element in set2:
        union.add(element)

    return union


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

union = set_union(set1, set2)

print(f"set 1 is {set1} and set 2 is {set2} and union is {union}")

