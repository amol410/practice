a = [1, 2, 3, 4, 5]
target = 9

found = False
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(f"The two numbers are {a[i]} and {a[j]} at indices {i} and {j}")
            found = True
            break
    if found:
        break

if not found:
    print("No two numbers sum up to the target")