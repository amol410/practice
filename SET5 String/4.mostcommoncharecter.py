# Write a program to find the most common character in a string.

string = "The quick brown fox jumps over the lazy dog. The dog is sleeping."
word = "the"

# Convert the string to lowercase for case-insensitive comparison
string = string.lower()
word = word.lower()

# Split the string into words
words = string.split()

# Count the occurrences of the word
count = 0
for w in words:
    if w == word:
        count += 1

print(f"The word '{word}' appears {count} times in the string.")