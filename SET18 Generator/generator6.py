# Implement a generator that generates a sequence of strings with random characters.

import random
import string

# Define the generator to yield random strings
def random_string_generator(count, length=6):
    characters = string.ascii_letters + string.digits  # Define possible characters (letters and digits)
    
    for _ in range(count):
        random_string = ''.join(random.choice(characters) for _ in range(length))
        yield random_string

# Example usage
random_strings = random_string_generator(5, 8)  # Generate 5 random strings of length 8

# Iterate through the generator and print random strings
for rand_str in random_strings:
    print(rand_str)


'''
g7Hd82Ja
L1pQe7Uz
qT9XbR5d
Z0Na5YxK
mF4u8WzP

'''