# Create a function to check if a string is an anagram of another string.

def is_anagram(str1, str2):
    # Remove whitespace and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Convert strings to lists and sort them
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    print(list1)
    list2.sort()
    print(list2)
    
    # Compare the sorted lists
    if list1 == list2:
        return True
    else:
        return False

# Test the function
string1 = "listen"
string2 = "silent"
string3 = "hello"

print(is_anagram(string1, string2))  # Output: True
print(is_anagram(string1, string3))  # Output: False