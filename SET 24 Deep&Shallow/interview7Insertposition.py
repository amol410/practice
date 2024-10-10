# insert position

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Test the function
solution = Solution()

# Example 1
nums1 = [1,3,5,6]
target1 = 5
result1 = solution.searchInsert(nums1, target1)
print(result1)


# Example 2
nums2 = [1,3,5,6]
target2 = 2
result2 = solution.searchInsert(nums2, target2)
print(result2)

# Example 3
nums3 = [1,3,5,6]
target3 = 7
result3 = solution.searchInsert(nums3, target3)
print(result3)