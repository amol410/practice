# Create a program that defines a function with a variable number of keyword arguments.

def display_variable_kwargs(**kwargs):
    """
    Displays the provided keyword arguments in a formatted way.

    Parameters:
    **kwargs: Arbitrary keyword arguments representing different pieces of information.
    """
    print("Provided Keyword Arguments:")
    if not kwargs:
        print("  No keyword arguments provided.")
    else:
        for key, value in kwargs.items():
            print(f"  {key.capitalize()}: {value}")

# Example usage
display_variable_kwargs(name="Alice", age=28, occupation="Engineer", city="San Francisco")
display_variable_kwargs()
display_variable_kwargs(hobby="Photography", language="Python")



"""
Provided Keyword Arguments:
  Name: Alice
  Age: 28
  Occupation: Engineer
  City: San Francisco

"""

"""
Provided Keyword Arguments:
  No keyword arguments provided.

"""

"""
Provided Keyword Arguments:
  Hobby: Photography
  Language: Python

"""