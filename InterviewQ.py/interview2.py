a = [1, 2, 3, 4, 5]
target = 9

found = False
for i, num1 in enumerate(a):
    for j, num2 in enumerate(a[i+1:], start=i+1):
        if num1 + num2 == target:
            print(f"The two numbers are {num1} and {num2} at indices {i} and {j}")
            found = True
            break
    if found:
        break

if not found:
    print("No two numbers sum up to the target")