#Create a function that accepts two numbers and returns their sum.

# Just Printing result by calling function
def add_numbers(a,b):
    print(a+b)
    
add_numbers(10,50) 

# practice - we can return multiple values 
def add_numbers(a,b):
    return a+b, a-b   # kya baat hai return k samne hi calculation

addition = add_numbers(10, 20)

print(addition)


# Return addition result
def add_numbers(a,b):
    return a+b
x = int(input("write the value of x:- "))
y = int(input("write the value of y:- "))

addition = add_numbers(x, y)

print(addition)


# Return and Print in same function
def add_numbers(a,b):
    print(a+b)
    return a-b
tryi = add_numbers(10,50) # returned a-b value captured here
print(tryi)


