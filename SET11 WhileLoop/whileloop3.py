# create a program to calculate factorial of a number 
# if i am making function for factorial, i need to iterate nth number
# and also i want to make product(multiple) of n numbers
# for iterating use I and for product use RESULT both = 1
# need to iterate till nth number right ? i <= nth

def factorial(n):
    if n < 0 :
        print("Factorial is not defined for negative numbers")
        return None
    
    result = 1
    i = 1

    while i <= n :
        result *= i
        i += 1
    return result

#example usage
num = int(input("Enter a non negative integer: "))
fact = factorial(num)

if fact is not None:
    print(f"factorial of {num} is {fact}")


# def factorial(n):
#     if n < 0:
#         print("cant calulate factorial of negative numbers")
#         return None
#     i = 1
#     result = 1

#     while i <= n:
#         result *= i
#         i = i + 1
#     return result    

# n = int(input("Write a number for factorial: "))
# fact = factorial(n)  

# print(f"factorial of number {n} is {fact} ")



# def factorial(n):
#     if n < 0:
#         print("Not defined for non negative numbers")
#         return None 
#     i = 1
#     result = 1 

#     while i <= n:
#         result *= i
#         i = i + 1
#     return result    

# n = int(input("non negative number: "))
# fact = factorial(n)

# print(f"factorial of {n} is {fact}")