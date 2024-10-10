# Create a function to check if a string is an anagram of another string.

def is_anagram(str1, str2):
    string1 = str1.replace(" ", "").lower()
    string2 = str2.replace(" ", "").lower()

    if len(string1) != len(string2):
        print("Not an anagram")
    
    st1 = sorted(string1)
    st2 = sorted(string2)

    if st1 == st2:
        print(f"{str1} and {str2} are anagram")
    

# Test the function
string1 = "listen"
string2 = "silent"
string3 = "hello"

print(is_anagram(string1, string2))  # Output: True
print(is_anagram(string1, string3))  # Output: False

# str1.replace(" ", "")
# str1.replace(" ", "").lower()
# list1.sort()