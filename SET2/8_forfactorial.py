# Implement a program to find the factorial of a number using a for loop.

def factorial(n):
    result = 1
    
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    
    for i in range(1, n+1):
        result *= i
    
    return result

# Example usage
num = int(input("Enter a non-negative integer: "))
fact = factorial(num)

if fact is not None:
    print(f"The factorial of {num} is: {fact}")