class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

# Test the function
solution = Solution()

# Example 1
nums1 = [3, 2, 3]
result1 = solution.majorityElement(nums1)


# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
result2 = solution.majorityElement(nums2)      