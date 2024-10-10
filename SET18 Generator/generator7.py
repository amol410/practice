# Write a Python generator that yields elements of a list in reverse order.

# Define the generator to yield elements of a list in reverse order
def reverse_list_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

# Example usage
my_list = [10, 20, 30, 40, 50]
reversed_elements = reverse_list_generator(my_list)

# Iterate through the generator and print elements in reverse order
for element in reversed_elements:
    print(element)
