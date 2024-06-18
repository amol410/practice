#11 Implement a program to find the second largest element in a list.


def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
            print(f"largest '{largest}', second_largest '{second_largest}'")
        elif num > second_largest and num < largest:
            second_largest = num
            print(f"largest '{largest}', second_largest '{second_largest}'")

    if second_largest == float('-inf'):
        return None

    return second_largest

numbers = [10, 5, 8, 22, 18, 21]

result = find_second_largest(numbers)

print("result is ", result)