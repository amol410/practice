# Implement a function that accepts a combination of positional and keyword arguments.

def mixed_arguments(*args, **kwargs):
    # Printing positional arguments
    print("Positional arguments:")
    for index, value in enumerate(args):
        print(f"  Argument {index + 1}: {value}")
    
    # Printing keyword arguments
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Example usage
mixed_arguments(1, "apple", 3.14, name="Alice", age=25, city="Paris")


'''
Positional arguments:
  Argument 1: 1
  Argument 2: apple
  Argument 3: 3.14

Keyword arguments:
  name: Alice
  age: 25
  city: Paris

'''