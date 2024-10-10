# # Input list
# L1 = ["1", "2", "2", "5", "3", "2", "5", "2", "4", "3"]

# # Empty dictionary to store counts of each element
# counts = {}

# # Manually count occurrences of each element
# for num in L1:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1

# # Filter out elements that appear more than once
# non_common_numbers = [num for num in counts if counts[num] == 1]

# print(non_common_numbers)

# # another way

# from collections import Counter

# # Input list
# L1 = ["1", "2", "2", "5", "3", "2", "5", "2", "4", "3"]

# # Count the occurrences of each element in the list
# counts = Counter(L1)

# # Filter out the elements that appear more than once
# non_common_numbers = [num for num, count in counts.items() if count == 1]

# print(non_common_numbers)


L1 = ["1", "2", "2", "5", "3", "2", "5", "2", "4", "3"]

counts = {}

for num in L1:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# list1 = []

# for num in counts:
#     if counts[num] == 1:
#         list1.append(num)
# print(list1) 

uniquee = [num for num in counts if counts[num] == 1]

print(uniquee)

