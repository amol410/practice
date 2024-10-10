# Implement a program to write data to a text file.

# Data to be written to the file
data = "Hello, this is a sample text."

# Open the file in write mode
with open('output.txt', 'w') as file:
    # Write the data to the file
    file.write(data)

print("Data has been written to the file.")
