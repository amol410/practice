# Write a function that accepts and prints an arbitrary number of positional arguments.

def print_positional_arguments(*args):
    print("Positional arguments:")
    for index, value in enumerate(args):
        print(f"  Argument {index + 1}: {value}")

# Example usage
print_positional_arguments(10, "hello", 3.14, True, [1, 2, 3])


'''
Positional arguments:
  Argument 1: 10
  Argument 2: hello
  Argument 3: 3.14
  Argument 4: True
  Argument 5: [1, 2, 3]

'''