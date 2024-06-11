def ifact(n):
    fact=1
    for i in range(1,n+1):
        fact = i * fact

    return fact

no=int(input('Enter the no : '))
res = ifact(no)
print(res)


def ifact(number):
    fact = 1
    for i in range(1, number+1):
        fact*= i
    return fact

number = int(input("Enter the number here :- "))

factorial = ifact(number)

print(factorial)
