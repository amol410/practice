#5 Write a program to remove a key from a dictionary.


my_dict = {
    'apple': 2,
    'banana': 3,
    'orange': 1,
    'grape': 5
}

print("Original Dictionary :-", my_dict)

key_to_remove = 'banana'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' has been removed")

print("Result is :- ", my_dict)



#practice

my_dict = {
    'apple': 2,
    'banana': 3,
    'orange': 1,
    'grape': 5
}

print(my_dict)

key_removal = 'banana'

if key_removal in my_dict:
    del my_dict[key_removal]
    print(f"here we '{key_removal}' removed")

print(my_dict)