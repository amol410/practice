# Implement a function to check if an element exists in a tuple.

def element_exists(tuple_data, element):
    if element in tuple_data:
        return True
    else:
        return False
    
# Example tuple
my_tuple = (1, 2, 3, 4, 5)

# Check if an element exists in the tuple
print(element_exists(my_tuple, 3))  # Output: True
print(element_exists(my_tuple, 6))  # Output: False    