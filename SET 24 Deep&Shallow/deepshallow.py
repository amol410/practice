# if we modify the nested list/object of shallow copy it changes original list/object.
# if we modify the nested list/object of deep copy it won't change original list/object. 

import copy

# Original list
original = ['apple', ['banana', 'cherry']]

# Shallow copy
shallow = copy.copy(original)

# Modify the nested list in the shallow copy
shallow[1][0] = 'grape'

print("Original:", original)
print("Shallow copy:", shallow)

#output
#Original: ['apple', ['grape', 'cherry']]
#Shallow copy: ['apple', ['grape', 'cherry']]


import copy

# Original list
original = ['apple', ['banana', 'cherry']]

# Deep copy
deep = copy.deepcopy(original)

# Modify the nested list in the deep copy
deep[1][0] = 'grape'

print("Original:", original)
print("Deep copy:", deep)

#Output
# Original: ['apple', ['banana', 'cherry']]
# Deep copy: ['apple', ['grape', 'cherry']]