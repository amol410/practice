# Lambda function to capitalize the first letter of each word in a sentence
capitalize_words = lambda sentence: ' '.join(word.capitalize() for word in sentence.split())

# Example usage
sentences = [
    "hello world, how are you?",
    "python is a great programming language",
    "lambda functions are powerful"
]

# Apply the lambda function to each sentence and print the results
for sentence in sentences:
    capitalized = capitalize_words(sentence)
    print(f"Original: {sentence}")
    print(f"Capitalized: {capitalized}")
    print()