# implement a function to check if a string is a palindrome.
def is_palindrome(string):
    # Reverse the string
    reversed_string = string[::-1]
    
    # Compare the original string with its reverse
    return string == reversed_string
# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome(""))  # Output: True
print(is_palindrome("madam"))  # Output: True

# Get the input string from the user
string = input("Enter a string: ")

# Reverse the string
reversed_string = string[::-1]

# Compare the original string with its reverse
if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")