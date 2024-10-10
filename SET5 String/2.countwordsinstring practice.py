#Write a Python program to count the occurrences of a specific word in a string.

def count_word_occurrences(string, word):
    st = string.lower()
    wd = word.lower()

    st = st.split()
    counter = st.count(word)
    print(counter)

# Example usage
string = "The quick brown fox jumps over the lazy dog . The dog is sleeping."
word = "dog"

occurrences = count_word_occurrences(string, word)

# string.lower()
# string.split()
# string.count(word)
# string.upper()

