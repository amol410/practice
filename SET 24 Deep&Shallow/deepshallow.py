# Use shallow copy when you only need to create a new container object but are 
# fine with sharing references to nested objects. Use deep 
# copy when you need a completely independent copy of an object and all its nested objects.

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