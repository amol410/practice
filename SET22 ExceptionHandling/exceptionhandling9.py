# Implement a program that handles a NameError exception.

def print_variable():
    try:
        # Attempt to print a variable that has not been defined
        print(undeclared_variable)
    except NameError as e:
        print(f"Caught a NameError: {e}")
        # Handle the error by defining the variable
        undeclared_variable = "Variable has been defined now!"
        print(undeclared_variable)

print_variable()
