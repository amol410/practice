import random

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", my_list)

# Shuffle the list using the Fisher-Yates algorithm
for i in range(len(my_list) - 1, 0, -1):
    # Generate a random index j between 0 and i (inclusive)
    j = random.randint(0, i)
    
    # Swap elements at index i and j
    my_list[i], my_list[j] = my_list[j], my_list[i]

print("Shuffled List:", my_list)


# or
# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", my_list)

# Shuffle the list using the Fisher-Yates algorithm
for i in range(len(my_list) - 1, 0, -1):
    # Generate a random index j between 0 and i (inclusive)
    j = i
    while j == i:
        j = (i * 45221 + 1) % (i + 1)
    
    # Swap elements at index i and j
    my_list[i], my_list[j] = my_list[j], my_list[i]

print("Shuffled List:", my_list) 