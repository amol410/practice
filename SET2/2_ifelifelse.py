# Create a program that checks if a number is positive, negative, or zero.

# normal

n = int(input("enter your number :- "))

if n > 0:
    print("number is positive")

elif n == 0:
    print("number is zero")

else:
    print("your number is negative")     





# next step (advance)
while True:
    n = input("Enter a number :- ")
    if n.lower() == "exit":
        break
    n = int(n)

    if n > 0:
        print("number is positive")

    elif n == 0:
        print("number is zero")

    else:
        print("your number is negative")        

