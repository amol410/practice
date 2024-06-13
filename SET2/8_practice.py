#8 Implement a program to find the factorial of a number using a for loop.

def factorial(n):
    result = 1

    if n < 0:
        print("Factorial of negative number is not given")

    for i in range(1, n+1):
        result *= i

    return result

num = int(input("Enter your number here:- "))
fact = factorial(num)

print(f"Factorial of your number '{num}' is '{fact}'")



# def factorial(n):
#     result = 1
#
#     if n < 0:
#         print("Factorial is not defined for negative numbers")
#         return None
#
#     for i in range(1, n+1):
#         result *= i
#
#     return result
#
#
# num = int(input("Enter your number:- "))
# fact = factorial(num)
#
# print(f"Your Factorial of number '{num}' is '{fact}' ")