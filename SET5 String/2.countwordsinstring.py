#Write a Python program to count the occurrences of a specific word in a string.

def count_word_occurrences(string, word):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    word = word.lower()
    
    # Split the string into words
    words = string.split()
    
    # Count the occurrences of the word
    count = words.count(word)
    
    return count

# Example usage
string = "The quick brown fox jumps over the lazy dog. The dog is sleeping."
word = "the"

occurrences = count_word_occurrences(string, word)
print(f"The word '{word}' appears {occurrences} times in the string.")