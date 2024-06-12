
# implement a function to check if a string is a palindrome.

def is_palindrome(string):

    reverse_string = string[::-1]

    return reverse_string == string

result = is_palindrome("madam")

print(result)



# check if a string is a palindrome.

string = input("write your string here :- ")

reverse_string = string[::-1]

if reverse_string == string:
    print("Your string is palindrome")
else:
    print("Your string is not palindrome")


