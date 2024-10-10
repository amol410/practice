# Create a program that defines a decorator to check if a user is logged in before accessing a function.

from functools import wraps

# Simulated user database and session
users = {
    "alice": "password123",
    "bob": "securepass456"
}
current_user = None

def login(username, password):
    global current_user
    if username in users and users[username] == password:
        current_user = username
        return True
    return False

def logout():
    global current_user
    current_user = None

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user is None:
            raise PermissionError("You must be logged in to access this function.")
        return func(*args, **kwargs)
    return wrapper

# Example usage
@login_required
def sensitive_function():
    print(f"Access granted. Welcome, {current_user}!")

# Test the decorator
def main():
    # Attempt to access function before logging in
    try:
        sensitive_function()
    except PermissionError as e:
        print(f"Error: {e}")

    # Log in and try again
    if login("alice", "password123"):
        print("Login successful")
        sensitive_function()
    else:
        print("Login failed")

    # Log out and try once more
    logout()
    try:
        sensitive_function()
    except PermissionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()