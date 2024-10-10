# Create a program that uses a function with keyword-only arguments to print a message.

def print_message(*, greeting="Hello", name="User"):
    """
    Prints a message using keyword-only arguments.

    Parameters:
    greeting (str): The greeting word to use. Default is "Hello".
    name (str): The name to address in the message. Default is "User".
    """
    print(f"{greeting}, {name}!")

# Example usage
print_message(greeting="Hi", name="Alice")
print_message(greeting="Welcome", name="Bob")
print_message(name="Charlie")  # Uses default greeting
print_message(greeting="Good morning")  # Uses default name
