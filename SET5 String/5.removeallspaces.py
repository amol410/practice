#Create a program to remove all the spaces from a string.

string = "Hello, world! This is a sample string with spaces."

# Initialize an empty string to store the result
result = ""

# Iterate over each character in the string
for char in string:
    # If the character is not a space, append it to the result string
    if char != " ":
        result += char

print("Original string:", string)
print("String without spaces:", result)