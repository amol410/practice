# Recursion is a way for a function to call itself to solve smaller parts of the same problem
# It's like breaking down a big task into smaller, more manageable tasks.

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        result = n * factorial(n-1)

    return result

fact = factorial(7)
print(fact)



# def factorial(n):
#     if n == 0:
#         result = 1

#     else:
#         result = n * factorial(n-1)
    
#     return result

# fact = factorial(5)    
# print(fact)



# def factorial(n):

#     if n == 0:
#         print("factorial of 0 is 1")
#         return 1
        
#     elif n < 0:
#         print("factorial is not defined for negative numbers")
#         return None
    
#     else:
#         result = n*factorial(n-1)

#     return result        


# fact = factorial(-1)

# print(fact)


# def factorial(n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return None
#     else:
#         result = n * factorial(n-1)

#     return result    
    
# fact = factorial(5)

# print(fact)


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result =  n * factorial(n-1)
    return result    


fact = factorial(5)

print(fact)           