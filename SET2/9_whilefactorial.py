# Create a program to calculate the factorial of a number using a while loop.

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    
    result = 1
    i = 1
    
    while i <= n:
        result *= i
        i += 1
    
    return result

# Example usage
num = int(input("Enter a non-negative integer: "))
fact = factorial(num)

if fact is not None:
    print(f"The factorial of {num} is: {fact}")