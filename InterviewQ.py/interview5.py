class Solution:
    def romanToInt(self, s):
        # Dictionary to store Roman numeral values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in s[::-1]:
            current_value = roman_values[char]
            
            # If current value is greater or equal to previous value, add it
            if current_value >= prev_value:
                total += current_value
            # If current value is less than previous value, subtract it
            else:
                total -= current_value
            
            prev_value = current_value
        
        return total

# Test the function
solution = Solution()

# Example 1
s1 = "III"
result1 = solution.romanToInt(s1)


# Example 2
s2 = "LVIII"
result2 = solution.romanToInt(s2)


# Example 3
s3 = "MCMXCIV"
result3 = solution.romanToInt(s3)
