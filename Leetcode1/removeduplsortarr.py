def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Initialize the pointer for unique elements
    k = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[k-1]:
            # Move the current element to the next position of unique elements
            nums[k] = nums[i]
            # Increment the count of unique elements
            k += 1
    
    return k

# Test the function
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)

print(k1)