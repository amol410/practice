#9 Create a program to calculate the factorial of a number using a while loop.


def factorial(n):
    result = 1
    i = 1

    if n < 0:
        print("You have entered negative number")
        return None

    while i <= n:
        result *= i  #result = result*i
        i += 1

    return result


num = int(input("Enter your non-negative number: - "))

fact = factorial(num)

print(f"Factorial of your number '{num}' is '{fact}'")















# def factorial(n):
#     result = 1
#     i = 1
#
#     if n < 0:
#         print("Factorial is not defined for negative numbers ")
#         return None
#
#     while i <= n:
#         result *= i  #result = result*i
#         i += 1
#
#     return result
#
#
# num = int(input("Enter a non-negative number:- "))
#
# fact = factorial(num)
#
# print(f"Factorial of your number '{num}' is {fact}")