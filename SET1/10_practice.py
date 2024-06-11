def factorial(number):
    fact = 1
    for i in range(1, 1+number):
        fact *= i
    return fact

number = int(input("Enter a number :-" ))

res = factorial(number)

print(res)