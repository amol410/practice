# Write a Python program that handles a ZeroDivisionError exception.

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        return result

# Example usage
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

result = divide_numbers(numerator, denominator)

if result is not None:
    print(f"Result: {numerator} / {denominator} = {result}")
