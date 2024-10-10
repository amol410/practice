# Implement a decorator that logs exceptions raised during the execution of a function.

import functools
import logging
import traceback
from datetime import datetime

def log_exception(logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Get the current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Create a detailed error message
                error_msg = f"Exception in {func.__name__} at {timestamp}:\n"
                error_msg += f"Type: {type(e).__name__}\n"
                error_msg += f"Message: {str(e)}\n"
                error_msg += "Traceback:\n"
                error_msg += "".join(traceback.format_tb(e.__traceback__))
                
                # Log the error
                logger.error(error_msg)
                
                # Re-raise the exception
                raise
        return wrapper
    return decorator

# Configure logging
logging.basicConfig(level=logging.ERROR, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app_errors.log')

# Example usage
@log_exception()
def divide(a, b):
    """Divide a by b."""
    return a / b

# Test the decorator
def main():
    try:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")
    except Exception as e:
        print(f"Caught exception: {e}")

    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except Exception as e:
        print(f"Caught exception: {e}")

    print("\nCheck the 'app_errors.log' file for detailed error logs.")

if __name__ == "__main__":
    main()