# Create a program that catches and re-raises an exception.

def process_data(data):
    try:
        # Example: division by zero
        result = 10 / data
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")
        # Re-raising the exception
        raise
    return result

try:
    process_data(0)
except ZeroDivisionError as e:
    print(f"Exception re-raised: {e}")
