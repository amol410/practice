# Implement a dictionary comprehension to create a dictionary from two lists of keys and values.

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
result = {k: v for k, v in zip(keys, values)}