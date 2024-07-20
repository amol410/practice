def decor(func):
    c = 25
    def inner(a,b):
            return a + b + c
    return inner

@decor
def summer(a,b):
    print(a+b)
result = summer(25,25)

print(result)