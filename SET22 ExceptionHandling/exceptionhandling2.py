# Create a program that catches a FileNotFoundError and displays a custom error message.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        
# Example usage
filename = input("Enter the name of the file you want to read: ")

read_file(filename)
