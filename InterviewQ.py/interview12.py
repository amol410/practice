# Count minimum swap to make string palindrome
def minSwap(s):
	strng = list(s)
	unmp = {}
	for i in strng:
		unmp[i] = unmp.get(i,0)+1
	odd = 0
	result = 0
	left = 0
	right = len(strng)-1
	for i in unmp:
		if unmp[i]%2 != 0:
			odd += 1
	# If we found more than one odd number
	if odd > 1:
		return -1
	while left < right:
		l = left
		r = right
		while strng[l] != strng[r]:
			r -= 1
		if l == r:
			# When we found odd element move towards middle
			strng[r],strng[r+1] = strng[r+1],strng[r]
			result += 1
			continue
		else:
			# Normal element move towards right of string
			while r < right:
				strng[r],strng[r+1] = strng[r+1],strng[r]
				r += 1
				result += 1
		left += 1
		right -= 1
	return result
s="aabcc"
print(minSwap(s))

# another approach

def minSwap(s):
    strng = list(s)
    left = 0
    right = len(strng) - 1
    result = 0

    while left < right:
        # If characters at left and right are equal, move inward
        if strng[left] == strng[right]:
            left += 1
            right -= 1
        else:
            # Find the matching character from the right side
            r = right
            while r > left and strng[r] != strng[left]:
                r -= 1

            # If we found the character, swap it until it reaches the correct position
            if r == left:
                # If no matching character found, this must be the odd character
                strng[left], strng[left + 1] = strng[left + 1], strng[left]
                result += 1
            else:
                # Swap the matching character towards the right position
                for i in range(r, right):
                    strng[i], strng[i + 1] = strng[i + 1], strng[i]
                    result += 1
                left += 1
                right -= 1

    return result

# Driver code
s = "aabcc"
print(minSwap(s))
