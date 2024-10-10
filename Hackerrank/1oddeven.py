# def check_weird(n):
#     if n % 2 == 1:
#         print("Weird")
#     else:
#         if 2 <= n <= 5:
#             print("Not Weird")
#         elif 6 <= n <= 20:
#             print("Weird")
#         elif n > 20:
#             print("Not Weird")

# # Example usage
# n = int(input("Enter a number: "))
# check_weird(n)

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2<n<5:
        print("Not Weird")
    elif n % 2 == 0 and 6<n<=20:
            print("Weird")
    elif n % 2 == 0 and n>20:
            print("Not Weird")


a = input("Enter your name here:")
x = ""
for i in range(len(a)):
    if a[i] == a[i].lower():
        x += a[i].upper()
    else:
        x += a[i].lower()
print(x)        


def is_leap(year):
   # A leap year is divisible by 400 or divisible by 4 but not by 100
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))




