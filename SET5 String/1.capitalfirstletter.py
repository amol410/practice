# Implement a function to capitalize the first letter of each word in a sentence.

sentence = "hello world, how are you?"

# Initialize an empty string to store the capitalized sentence
capitalized_sentence = ""

# Split the sentence into words
words = sentence.split()
print(words)

# Iterate over each word in the sentence
for word in words:
    # Capitalize the first letter of the word
    capitalized_word = word[0].upper() + word[1:]
    # Append the capitalized word to the string, followed by a space
    capitalized_sentence += capitalized_word + " "

# Remove the trailing space from the capitalized sentence
capitalized_sentence = capitalized_sentence.strip()

# Print the original and capitalized sentences
print("Original sentence:", sentence)
print("Capitalized sentence:", capitalized_sentence)



sentence = "hello world, how are you?"

capitalized_sentence = ""

words = sentence.split()


for word in words:
    capitalword = word[0].upper() + word[1:]

    capitalized_sentence += capitalword + " "


print(sentence)
print(capitalized_sentence)    