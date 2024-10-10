# Write a Python program that handles an IndexError exception.

def access_list_element(my_list, index):
    try:
        # Attempt to access the element at the given index
        element = my_list[index]
        print(f"Element at index {index} is: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range. The list has {len(my_list)} elements.")

# Example usage
my_list = [10, 20, 30, 40, 50]
index = int(input("Enter the index you want to access: "))

access_list_element(my_list, index)
