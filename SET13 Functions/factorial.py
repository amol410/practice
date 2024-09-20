# Write a Python function to calculate the factorial of a number.

def factorial(n):
    if n < 0:
        print("factorial is not defined for negative numbers")
        return None
    
    
    result = 1

    for i in range(1, n+1):
        if i <= n:
            result *= i
    return result

num = 5

fact = factorial(num)    

print(fact)