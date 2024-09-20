class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1, nums2, and the merged array
        p1 = m - 1  # Last element in nums1
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last position in merged array

        # Merge arrays from back to front
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# Test the function
solution = Solution()
# Example 1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
solution.merge(nums1, m, nums2, n)


# Example 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
