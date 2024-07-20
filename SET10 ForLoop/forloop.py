# factorial of number using for loop
# approach >> need to iterate till nth number as its factorial function
# for using for loop I should start with 1 hence range(1, n+1)
# result *= i 

def factorial(n):
    if n < 0 :
        print("Factorial is not defined for negative numbers")
        return None
    
    result = 1
    
    for i in range(1, n+1):
        result *= i
        
    return result

#example usage
n = int(input("Enter a non negative integer: "))
fact = factorial(n)

if fact is not None:
    print(f"factorial of {n} is {fact}")



# def factorial(n):
#     if n < 0 :
#         print("Factorial is not defined for negative numbers")
#         return None
    
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result    

# #example usage
# n = int(input("Enter a non negative integer: "))
# fact = factorial(n)

# if fact is not None:
#     print(f"factorial of {n} is {fact}")    

# def factorial(n):
#     if n < 0 :
#         print("Not defined for non negative")
#         return None
    
#     result = 1
#     for i in range(1, n+1):
#         result = result*i
#     return result    


# #example usage
# n = int(input("Enter a non negative integer: "))
# fact = factorial(n)

# if fact is not None:
#     print(f"factorial of {n} is {fact}")    