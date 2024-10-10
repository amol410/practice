# Implement a Python function that accepts keyword arguments to display user information (name, age, etc.).

def display_user_info(**kwargs):
    """
    Displays user information provided as keyword arguments.

    Parameters:
    **kwargs: Arbitrary keyword arguments representing user information.

    Example:
    display_user_info(name="John Doe", age=30, email="john@example.com")
    """
    print("User Information:")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")

# Example usage
display_user_info(name="John Doe", age=30, email="john@example.com", city="New York")



'''
User Information:
  Name: John Doe
  Age: 30
  Email: john@example.com
  City: New York

'''