# import copy 

# original = ['apple',['grapes','banana']]



# class fname:
#     def __init__(self, fullname):
#         self.fullname = fullname

#     def child(self):
#         print(f"hello {self.fullname}") 

# class child(fname):
#      def track(self):
#          pass

# f = fname("amol")

# f.child()


# Write a function to count the number of unique digits in a number - 

# def counter(number):
#     i = 0
#     k = 0
#     for num in number:
#         if num[i] != num[k]:
#             k


# list1 = '123'

# result = counter(list1)
# eg 111 -> 1

# 121 -> 2

# 123 -> 3
 
list1= [8,3,5,8,5,7,4,6,9]
list3 = list1.copy()
a = 5
list2 =[]
for i, num in enumerate(list1):
    if list1[i] == a:
        list2.append(i)
list2 =list2

for i, num in enumerate(list1):
    if i == list2[0]:
        del list1[i]
       
list1 = int(''.join(map(str, list1)))
print(list1) 

for i, num in enumerate(list3):
    if i == list2[1]:
        del list3[i]
list3 = int(''.join(map(str, list3)))
print(list3)

if list1 > list3:
    print("first 5 removal is greater")
else:
    print("second 5 removal is greater")
    






