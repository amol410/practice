# Function to find the most common character in a string

def most_common_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)        

    most_common = max(char_count, key=char_count.get)
    # least_common = min(char_count, key=char_count.get)
    # print(least_common)
    
    return most_common, char_count[most_common]

# Test the function
input_string = "hello world"
most_common, count = most_common_char(input_string)
print(f"The most common character is '{most_common}' which appears {count} times.")
