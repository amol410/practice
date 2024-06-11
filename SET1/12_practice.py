# without using function

list = [1,2,3,4,5,6,7] 

Total = 0

for i in list:
    Total += i

print (Total)    


# with using function
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
result = sum_of_list(my_list)
print("Sum of the elements:", result)

# with using function
def sum_of_list(list):
    Total = 0
    for i in list:
        Total += i

    return Total

list = [1,2,3,4,5,6,7,8] 

result = sum_of_list(list)

print("sum of the total elements in list:" , result)




def sum_of_list(list):
    Total = 0
    for i in list:
        Total += i
    return Total

list = [1,2,3,4,5,6,7,8]
result = sum_of_list(list)

print(result)


 

