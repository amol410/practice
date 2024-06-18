# Create a program that counts the number of vowels and consonants in a string.

# Define the input string
input_string = "Hello, World! This is a sample string."

# Define vowels and consonants
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# Initialize counters
vowel_count = 0
consonant_count = 0

# Iterate over each character in the string
for char in input_string:
    # Check if the character is alphabetic
    if char.isalpha():
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
        # Check if the character is a consonant
        elif char in consonants:
            consonant_count += 1

# Print the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)