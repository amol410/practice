#7 Create a program that checks if a number is positive, negative, or zero.

while True:
    n = input("Enter your input here :- ")
    if n.lower() == 'exit':
        break
    n = int(n)

    if n > 0 :
        print ("Your number is Positive")

    elif n==0:
        print("Your number is Zero")

    else:
        print("Your number is Negative")




# while True:
#     n = input("Enter a number :- ")
#     if n.lower() == 'exit':
#         break
#     n = int(n)
#
#     if n > 0:
#         print("Your number is positive")
#
#     elif n == 0:
#         print("Your number is Zero")
#
#     else:
#         print("Your number is Negative")





# n = int(input("Enter a number here :- "))
#
# if n > 0:
#     print("Your number is Positive")
#
# elif n == 0:
#     print("Your number is Zero")
#
# else:
#     print("Your number is negative")


