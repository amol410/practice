# Implement a class "BankAccount" with a private attribute for account balance. Provide methods to deposit and withdraw money while encapsulating the balance.

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number  # Protected attribute
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
            else:
                return "Insufficient funds. Withdrawal canceled."
        else:
            return "Invalid withdrawal amount. Please withdraw a positive amount."

    def get_balance(self):
        return f"Current balance: ${self.__balance:.2f}"

    def get_account_info(self):
        return f"Account Number: {self._account_number}, {self.get_balance()}"

# Usage example
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount("1234567890", 1000)

    # Demonstrate account operations
    print(account.get_account_info())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(2000))  # Attempt to withdraw more than balance
    print(account.deposit(-100))   # Attempt to deposit a negative amount
    print(account.get_balance())

    # Demonstrate encapsulation
    try:
        print(account.__balance)  # This will raise an AttributeError
    except AttributeError as e:
        print(f"Error: {e}")

    # Accessing protected attribute (not recommended, but possible)
    print(f"Account number: {account._account_number}")

    # Attempting to modify private attribute directly (creates a new attribute)
    account.__balance = 1000000
    print(account.get_balance())  # The actual balance remains unchanged