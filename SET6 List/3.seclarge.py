# Implement a program to find the second largest element in a list.

def find_second_largest(lst):
    if len(lst) < 2:
        return None

    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest

# Example usage
numbers = [10, 5, 8, 20, 15, 20]
result = find_second_largest(numbers)
print("The second largest element is:", result)


def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')

    for element in numbers:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element <largest:
            second_largest = element
    return second_largest        


numbers = [10, 5, 8, 20, 15, 20]
result = find_second_largest(numbers)
print(f"result is here {result}")