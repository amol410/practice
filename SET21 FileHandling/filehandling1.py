# Write a Python program to read a text file and display its content.

# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Display the content
print(content)
