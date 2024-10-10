class Solution:
    def removeElement(self, nums, val):
        k = 0  # Counter for elements not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

# Test the function
solution = Solution()

# Example 1
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = solution.removeElement(nums1, val1)

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = solution.removeElement(nums2, val2)