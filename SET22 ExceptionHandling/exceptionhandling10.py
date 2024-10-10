# Write a Python program to handle exceptions for user input errors (e.g., ValueError).

def get_integer_input():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            print(f"You entered: {user_input}")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input! Please enter a valid integer. Error: {e}")

get_integer_input()
