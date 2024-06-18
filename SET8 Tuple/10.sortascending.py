# Write a program to check if a tuple is sorted in ascending order.



def is_sorted_ascending(tuple_data):
    return tuple_data == tuple(sorted(tuple_data))

# Example usage
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 2, 1, 4, 5)
tuple3 = (1, 2, 3, 4, 4)

print("Tuple 1:", tuple1)
print("Is Tuple 1 sorted in ascending order?", is_sorted_ascending(tuple1))

print("\nTuple 2:", tuple2)
print("Is Tuple 2 sorted in ascending order?", is_sorted_ascending(tuple2))

print("\nTuple 3:", tuple3)
print("Is Tuple 3 sorted in ascending order?", is_sorted_ascending(tuple3))