class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums) <= 2:
            return len(nums)

        # Initialize the pointer for the position to place the next element
        k = 2
        
        # Iterate through the array starting from the third element
        for i in range(2, len(nums)):
            # If the current element is different from the element two positions back
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k
nums = [1, 1, 1, 2, 2, 3]
solution = Solution()
k1 = solution.removeDuplicates(nums)  

nums1 = [0,0,1,1,1,1,2,3,3]
solution1 = Solution()
k2=solution1.removeDuplicates(nums1)
            