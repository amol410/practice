#10 Implement a function to check if an element exists in a tuple.

def element_exists(tuple_data, element):

    if element in tuple_data:
        return True
    else:
        return False

my_tuple = (1,2,3,4,5)

result = element_exists(my_tuple, 6)

print(result)


















# def element_exists(tuple_data, element):
#
#     if element in tuple_data:
#         return True
#     else:
#         return False
#
# my_tuple = (1,2,3,4,5)
#
# element_exist = element_exists(my_tuple,6)
#
# print(element_exist)