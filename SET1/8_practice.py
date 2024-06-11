# practice 1
def key_exists(dictionary, key):
    return key in dictionary


my_dict = {'a': 1, 'b': 2, 'c': 3}

print(key_exists(my_dict, 'a'))
print(key_exists(my_dict, 'b'))
print(key_exists(my_dict, 'd'))


my_dict = {'a': 1, 'b': 2, 'c': 3}

if 'a' in my_dict:
    print(my_dict['a'])

