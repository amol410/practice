class solution:
    def LengthOfLastWord(self,s):
        
        s = s.rstrip()
        

        last_space = s.rfind(' ')

        x = len(s) - last_space - 1

        return x
        
s1 = "Hello World how's you doingggg  "

solution = solution()

result = solution.LengthOfLastWord(s1) 

print(result)