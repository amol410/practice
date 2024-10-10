# Input list
list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Dictionary to store the grouped anagrams
anagram_groups = {}

# Loop through each word in the list
for word in list1:
    # Sort the word and use the sorted word as a key
    sorted_word = ''.join(sorted(word))
    
    # If the sorted word is not a key in the dictionary, initialize it with an empty list
    if sorted_word not in anagram_groups:
        anagram_groups[sorted_word] = []
    
    # Append the original word to the list corresponding to the sorted word
    anagram_groups[sorted_word].append(word)

# Get the grouped anagrams as a list of lists
output = list(anagram_groups.values())

print(output)



# another way with import


from collections import defaultdict

# Input list
list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Dictionary to store the grouped anagrams
anagram_groups = defaultdict(list)

# Loop through each word in the list
for word in list1:
    # Sort the word and use the sorted word as a key
    sorted_word = ''.join(sorted(word))
    anagram_groups[sorted_word].append(word)

# Get the grouped anagrams as a list of lists
output = list(anagram_groups.values())

print(output)
