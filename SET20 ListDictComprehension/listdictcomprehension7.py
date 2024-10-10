# Create a program that uses list comprehension to generate a list of words with more than 5 characters from a sentence.

def long_words(sentence):
    return [word for word in sentence.split() if len(word) > 5]

# Example usage
sample_sentence = "The quick brown fox jumps over the lazy dog"
result = long_words(sample_sentence)
print(result)