# Implement a program to find the frequency of all elements in a tuple.

def frequency_of_elements(tuple_data):
    frequency = {}
    for item in tuple_data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    return frequency

# Example usage
my_tuple = (1, 2, 3, 2, 4, 1, 2, 3, 2, 4, 4)
result = frequency_of_elements(my_tuple)
print("Frequency of elements in the tuple: ", result)
for item, count in result.items():
    print(f"{item}: {count}")