# Write a function to find the longest word in a sentence.

def find_longest_word(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Initialize variables to store the longest word and its length
    longest_word = ""
    max_length = 0
    
    # Iterate over each word in the list of words
    for word in words:
        # Remove any punctuation marks from the word
        word = word.strip(".,!?;:")
        
        # Check if the current word is longer than the current longest word
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
longest = find_longest_word(sentence)
print("Longest word:", longest)