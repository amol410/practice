# Write a Python program to find the product of all elements in a tuple.

def product_of_tuple(tuple_data):
    product = 1
    for item in tuple_data:
        product *= item
    return product

# Example usage
my_tuple = (2, 3, 4, 5)
result = product_of_tuple(my_tuple)
print(f"The product of all elements in the tuple is: {result}")