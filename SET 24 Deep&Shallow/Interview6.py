# Check if the list Contains duplicates ?
class solution:
    def containduplicates(self, nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        
                
solution = solution()
nums = [1,2,3]
result = solution.containduplicates(nums)
print(result)