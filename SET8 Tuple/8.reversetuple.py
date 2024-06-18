# Create a function that returns the reverse of a tuple.


def reverse_tuple(tuple_data):
    return tuple(reversed(tuple_data))

# Example usage
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(my_tuple)
print("Original tuple:", my_tuple)
print("Reversed tuple:", reversed_tuple)