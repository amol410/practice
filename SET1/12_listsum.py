# Create a program to calculate the sum of all elements in a list using a for loop.

list = [1,2,3,4,5,6,7] 

total = 0

for i in list: 
# for i in len(list) completely different & for i, num in enumerate(list) is different
    
    total += i

print(total)


# using function 
def sum_of_list(list):
    Total = 0
    for i in list:
        Total += i

    return Total

list = [1,2,3,4,5,6,7,8] 

result = sum_of_list(list)

print("sum of the total elements in list:" , result)