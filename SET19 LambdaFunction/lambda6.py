# Implement a lambda function to extract the last word from a list of sentences.

# List of sentences
sentences = ["Hello world", "Lambda functions are useful", "Python is fun", "Extract the last word"]

# Using a lambda function to extract the last word from each sentence
last_words = list(map(lambda sentence: sentence.split()[-1], sentences))

# Output the list of last words
print("Last words:", last_words)


# output Last words: ['world', 'useful', 'fun', 'word']
