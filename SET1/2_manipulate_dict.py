my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# for key in my_dict:
#     print(key)

# name = my_dict['name']
# age = my_dict['age']

# print(name)
# print(age)

# print(my_dict.get('name'))

# for value in my_dict.values():
#     print(value)

# keys = my_dict.keys()
# items = my_dict.items()
# values = my_dict.values()

# print(items)
# print(values)
# print(keys)


for key, value in my_dict.items():
    print(key, value)  # Output: name Alice, age 

if 'age' in my_dict:
    print('age is present') 


# dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# new_dict = {key: value.upper() if isinstance(value, str) else value for key, value in dict.items()}
# print(new_dict)  # Output: {'name': 'ALICE', 'age': 30, 'city': 'NEW YORK'}
