# Create a program that uses list comprehension to extract the vowels from a string.

def extract_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string if char in vowels]

# Example usage
input_string = "Hello, World!"
result = extract_vowels(input_string)
print(result)