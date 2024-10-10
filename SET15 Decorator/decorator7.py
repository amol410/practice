# Create a Python decorator that encrypts the result of a function before returning it.

from functools import wraps
import base64
from cryptography.fernet import Fernet

def encrypt_result(key=None):
    if key is None:
        key = Fernet.generate_key()
    
    fernet = Fernet(key)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Convert result to string if it's not already
            if not isinstance(result, str):
                result = str(result)
            
            # Encrypt the result
            encrypted_result = fernet.encrypt(result.encode())
            
            # Return base64 encoded encrypted result
            return base64.b64encode(encrypted_result).decode()
        
        # Attach the key to the function for demonstration purposes
        # In a real-world scenario, you'd want to manage this key more securely
        wrapper.key = key
        
        return wrapper
    return decorator

# Example usage
@encrypt_result()
def get_sensitive_data(user_id):
    """Simulate fetching sensitive data for a user."""
    return f"Sensitive data for user {user_id}: SSN: 123-45-6789, Credit Card: 1234-5678-9012-3456"

# Function to decrypt the result (for demonstration)
def decrypt_result(encrypted_result, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(base64.b64decode(encrypted_result))
    return decrypted.decode()

# Test the decorator
def main():
    user_id = 12345
    encrypted_data = get_sensitive_data(user_id)
    print(f"Encrypted result: {encrypted_data}")
    
    # Decrypt and print the result
    decrypted_data = decrypt_result(encrypted_data, get_sensitive_data.key)
    print(f"Decrypted result: {decrypted_data}")

if __name__ == "__main__":
    main()