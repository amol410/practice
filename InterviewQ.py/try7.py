# remove nth charecter from a string 

s = "wonderful"
n = 3
new = ""

for i in range(len(s)):
    if i != n:
        new += s[i]

print(new)
