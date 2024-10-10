# move zeroes
class Solution:
    def movezeroes(self, nums):
        prev_idx = 0  # Pointer to track the position of the last non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap elements
                nums[prev_idx], nums[i] = nums[i], nums[prev_idx]
                prev_idx += 1  # Move the pointer to the next position

# Create an instance of the Solution class
solution = Solution()

# Test input
inputt = [0, 1, 0, 3, 12]

# Call the movezeroes method
solution.movezeroes(inputt)

# Print the modified list
print(inputt)
