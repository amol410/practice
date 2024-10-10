# Function to find the most common character in a string

def most_common_char(input_string):
    # Dictionary to store the count of each character
    char_count = {}
    
    # Iterate through the string to count each character
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    
    # Find the character with the highest count
    most_common = max(char_count, key=char_count.get)
    
    return most_common, char_count[most_common]

# Test the function
input_string = "hello world"
most_common, count = most_common_char(input_string)
print(f"The most common character is '{most_common}' which appears {count} times.")
