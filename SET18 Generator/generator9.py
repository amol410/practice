# Implement a generator that yields the elements of a list in random order.

import random

# Define the generator to yield elements of a list in random order
def random_order_generator(lst):
    indices = list(range(len(lst)))  # Create a list of indices
    random.shuffle(indices)          # Shuffle the indices
    
    for i in indices:
        yield lst[i]

# Example usage
my_list = [10, 20, 30, 40, 50]
random_elements = random_order_generator(my_list)

# Iterate through the generator and print elements in random order
for element in random_elements:
    print(element)


'''
30
10
50
20
40

'''