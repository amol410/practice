#Implement a program to replace all occurrences of a specific word in a string with another word.

# Define the input string
input_string = "The quick brown fox jumps over the lazy dog. The fox is quick."

# Define the word to be replaced and the replacement word
old_word = "quick"
new_word = "fast"

# Split the string into a list of words
words = input_string.split()

# Initialize an empty list to store the modified words
modified_words = []

# Iterate over each word in the list of words
for word in words:
    # Check if the current word matches the word to be replaced
    if word.lower() == old_word.lower():
        # If there is a match, append the replacement word to the modified_words list
        modified_words.append(new_word)
        print(modified_words)
    else:
        # If there is no match, append the original word to the modified_words list
        modified_words.append(word)

# Join the modified words back into a string
modified_string = " ".join(modified_words)

# Print the original string and the modified string
print("Original string:", input_string)
print("Modified string:", modified_string)


# above code is first occurance only here all occurance code is 

# Define the input string
input_string = "The quick brown fox jumps over the lazy dog. The fox is quick."

# Define the word to be replaced and the replacement word
old_word = "quick"
new_word = "fast"

# Replace all occurrences of the old word with the new word
modified_string = input_string.replace(old_word, new_word)

# Print the original string and the modified string
print("Original string:", input_string)
print("Modified string:", modified_string)