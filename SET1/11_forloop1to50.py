# For Loop
# Write a program to print all even numbers from 1 to 50 using a for loop.

n = int(input('Enter a number from 2 to 50 :- ' ))

# you can pass n instead of 51
for i in range(1, 51):
    if i % 2 == 0:
        print(i)