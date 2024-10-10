# Write a Python function that demonstrates the use of *args and **kwargs in function definitions.

def demonstrate_args_kwargs(*args, **kwargs):
    # Printing all positional arguments
    print("Positional arguments (*args):")
    for index, value in enumerate(args):
        print(f"  args[{index}] = {value}")
    
    # Printing all keyword arguments
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

# Example usage
demonstrate_args_kwargs(1, 2, 3, name="Alice", age=30, city="New York")


#output will be
# Positional arguments (*args):
#   args[0] = 1
#   args[1] = 2
#   args[2] = 3

# Keyword arguments (**kwargs):
#   name = Alice
#   age = 30
#   city = New York
