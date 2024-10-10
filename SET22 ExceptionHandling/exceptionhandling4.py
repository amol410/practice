# Write a Python program to catch multiple exceptions in a try-except block.

def process_file_and_divide():
    try:
        # Attempt to open a file
        filename = input("Enter the file name to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully.")

        # Ask for two numbers to perform division
        numerator = float(input("Enter a number for the numerator: "))
        denominator = float(input("Enter a number for the denominator: "))
        
        # Perform division
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

# Example usage
process_file_and_divide()
