# Implement a program that uses a finally block to ensure a resource is properly closed.

def read_file(filename):
    try:
        # Attempt to open the file
        file = open(filename, 'r')
        # Read the file content
        content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block will always execute to ensure the file is closed
        if 'file' in locals() and not file.closed:
            file.close()
            print(f"The file '{filename}' has been closed.")
        else:
            print(f"No file was opened or the file was already closed.")

# Example usage
filename = input("Enter the filename to open: ")
read_file(filename)
