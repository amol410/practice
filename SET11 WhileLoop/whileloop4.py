def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num

# Example usage
original_num = 12345
result = reverse_number(original_num)
print(f"Original number: {original_num}")
print(f"Reversed number: {result}")