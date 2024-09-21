# Write a lambda function to filter out words from a list of strings based on their length.

# Lambda function to filter words based on length
filter_words = lambda words, length: list(filter(lambda word: len(word) == length, words))

# Example word list
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Filter words of different lengths
words_length_5 = filter_words(word_list, 5)
words_length_3 = filter_words(word_list, 3)
words_length_10 = filter_words(word_list, 10)

print(f"Original list: {word_list}")
print(f"Words with 5 letters: {words_length_5}")
print(f"Words with 3 letters: {words_length_3}")
print(f"Words with 10 letters: {words_length_10}")

# Example of using the lambda function in a list comprehension
lengths_to_filter = [3, 5, 6]
filtered_lists = [filter_words(word_list, length) for length in lengths_to_filter]

print("\nFiltering multiple lengths:")
for length, filtered in zip(lengths_to_filter, filtered_lists):
    print(f"Words with {length} letters: {filtered}")