# remove charecters at even indices 

# s = "wonderful"

# new_string = ""

# for i in range(len(s)):
#     if i % 2 == 0:
#         new_string += s[i]

# print(new_string)        

s = "wonderful"

new_string = ""

for i in range(len(s)):
    if i % 2 == 0:
        new_string += s[i]

print(new_string)