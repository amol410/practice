#Create a program to remove all the spaces from a string.

string = "Hello, world! This is a sample string with spaces."

result = ""

for char in string:
    if char != " ":
        result += char
        

print("Original string:", string)
print("String without spaces:", result)