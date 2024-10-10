# # Decorator function that adds 'c' to the result
# def add_c(c):
#     def decorator(func):
#         def wrapper(a, b):
#             result = func(a, b)  # Calls the original function
#             return result + c  # Adds 'c' to the result
#         return wrapper
#     return decorator

# # Function that adds 'a' and 'b'
# @add_c(10)  # Adding 'c' (for example, 10)
# def add(a, b):
#     return a + b

# # Test the function
# result = add(5, 3)  # (5 + 3) + 10 = 18
# print(result)  # Output: 18

# def add_c(c):
#     def decorator(func):
#         def wrapper(a, b):
#             result = func(a, b)
#             return result + c
#         return wrapper
#     return decorator

# @add_c(8)
# def add(a,b):
#     return a + b

# result = add(5, 3)

# print(result)

def add_c(c):
    def decorator(func):
        def wrapper(a,b):
            result = func(a,b)
            return result + c
        return wrapper
    return decorator

@add_c(8)
def add(a, b):
    return a + b

result = add(5, 9)
print(result)