#6 Write a program to find the intersection of two sets.

def set_intersection(set1,set2):
    intersection = set()

    for element in set1:
        if element in set2:
            intersection.add(element)

    return intersection




set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

intersection = set_intersection(set1, set2)

print(set1)
print(set2)
print(intersection)



# practice

def set_intersection(set1, set2):
    intersection = set()

    for element in set1:
        if element in set2:
            intersection.add(element)

    return intersection


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

intersection = set_intersection(set1, set2)

print("set 1 :", set1)
print("set 2 :", set2)
print("intersection :", intersection)

