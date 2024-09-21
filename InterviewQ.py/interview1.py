# practiced 3 times 

# def cal_numbers(a, target):

#     seen = {}

#     for i, num in enumerate(a):
#         if target - num in seen:
#             return [seen[target-num],i]
#         elif num not in seen:
#             seen[num] = i

#     return seen    

# a = [1, 2, 3, 4, 5]
# target = 9

# fact = cal_numbers(a,target)

# print(fact)




# def calcium(targ, b):
    
#     seen = {}

#     for i, num in enumerate(b):
#         if targ - num in seen:
#             return [seen[targ-num], i]
#         elif num not in seen:
#             seen[num] = i

#     return seen        


# beb = 9
# bik = [1,4,6,7,5]
# calc = calcium(beb, bik)

# print(calc)


# def twosum(a, target):

#     seen = {}

#     for i, num in enumerate(a):
#         if target-num in seen:
#             return [seen[target-num], i]
#         elif num not in seen:
#             seen[num] = i
#     return seen        

# a = [4,3,2,1,9,8,7,6,5]
# target = 15

# sumindex = twosum(a, target)    

# print(sumindex)

def twosum(a, target):
    seen = {}

    for i, num in enumerate(a):
        if target - num in seen:
            return [seen[target-num], i]
        elif num not in seen:
            seen[num] = i
    return seen        


b = [7,4,5,6,3,2,1,9,8]
untarget = 13
toindex = twosum(b, untarget) 

print(toindex)