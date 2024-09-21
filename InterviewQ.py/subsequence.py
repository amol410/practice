# class Solution:
#     def isSubsequence(self, s, t):
#         i = 0
#         j = 0
      
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j +=1
#         return i == len(s)        


# solution = Solution()
# s1, t1 = "abc", "ahbgdc"
# result1 = solution.isSubsequence(s1, t1)





# class soln:
#     def issub(self, a, b):
#         i = 0
#         j = 0

#         while i < len(a) and j < len(b):
#             if a[i] == b[j]:
#                 i += 1
#             j += 1

#         return i == len(a)

# sol = soln()
# a = "hizk"
# b = "abcdefghijklmn"
# stc = sol.issub(a, b)

# print(stc)





# class soln:
#     def issub(self, a, b):
#         i = 0
#         j = 0
#         while i < len(a) and j < len(b):
#             if a[i] == b[j]:
#                 i +=1
#             j += 1 

#         return i == len(a)           


# sol = soln()
# a = "bhik"
# b = "abcdefghijklmn"
# stc = sol.issub(a, b)

# print(stc)




class solution:
    def issubsequence(self, a, b):
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i +=1
            j +=1
        return i == len(a)

solution = solution()
a = "bhik"
b = "abcdefghijklmn"
stc = solution.issubsequence(a, b)

print(stc)        