def cal_numbers(a, target):

    seen = {}

    for i, num in enumerate(a):
        if target - num in seen:
            return [seen[target-num],i]
        elif num not in seen:
            seen[num] = i

    return seen    

a = [1, 2, 3, 4, 5]
target = 9

fact = cal_numbers(a,target)

print(fact)