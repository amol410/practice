# Write a decorator that ensures a function is only executed during specific hours of the day.

from functools import wraps
from datetime import datetime, time

def restrict_to_hours(start_hour, end_hour):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.now().time()
            start = time(start_hour, 0)
            end = time(end_hour, 0)
            
            if start <= current_time < end:
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Function {func.__name__} can only be executed between {start_hour}:00 and {end_hour}:00")
        return wrapper
    return decorator

# Example usage
@restrict_to_hours(9, 17)  # Restrict to 9 AM to 5 PM
def business_hours_task():
    """A task that should only run during business hours."""
    return "Task executed successfully during business hours."

# Test function to simulate different times
def test_at_time(hour, minute):
    # Mock the datetime.now() method to return a specific time
    original_now = datetime.now
    datetime.now = lambda: datetime(2023, 1, 1, hour, minute)
    
    try:
        result = business_hours_task()
        print(f"Time: {hour:02d}:{minute:02d} - {result}")
    except ValueError as e:
        print(f"Time: {hour:02d}:{minute:02d} - Error: {e}")
    finally:
        # Restore the original datetime.now method
        datetime.now = original_now

# Test the decorator
def main():
    print("Testing business_hours_task at different times:")
    test_times = [
        (8, 59),  # Just before business hours
        (9, 0),   # Start of business hours
        (12, 0),  # Middle of business hours
        (16, 59), # Just before end of business hours
        (17, 0),  # End of business hours
        (20, 0)   # Well after business hours
    ]
    
    for hour, minute in test_times:
        test_at_time(hour, minute)

if __name__ == "__main__":
    main()