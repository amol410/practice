# Create a program that raises a custom exception and handles it using try-except.

# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(f"Error: {number} is a negative number!")
    else:
        print(f"{number} is a valid positive number.")

# Main function to demonstrate raising and catching the custom exception
def main():
    try:
        number = float(input("Enter a positive number: "))
        check_positive_number(number)
    except NegativeNumberError as e:
        print(e)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

# Example usage
main()
