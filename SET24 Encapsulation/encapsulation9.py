# Implement a class "Bank" that manages multiple bank accounts with private account balances. Provide methods to encapsulate account balances and perform transactions.

class Bank:
    def __init__(self):
        self.__accounts = {}  # Private dictionary to store account balances

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.__accounts:
            raise ValueError("Account already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__accounts[account_number] = initial_balance
        print(f"Account {account_number} created with balance ${initial_balance:.2f}.")

    def deposit(self, account_number, amount):
        if account_number not in self.__accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__accounts[account_number] += amount
        print(f"${amount:.2f} deposited into account {account_number}. New balance: ${self.__accounts[account_number]:.2f}.")

    def withdraw(self, account_number, amount):
        if account_number not in self.__accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.__accounts[account_number] < amount:
            raise ValueError("Insufficient funds.")
        self.__accounts[account_number] -= amount
        print(f"${amount:.2f} withdrawn from account {account_number}. New balance: ${self.__accounts[account_number]:.2f}.")

    def get_balance(self, account_number):
        if account_number not in self.__accounts:
            raise ValueError("Account does not exist.")
        return self.__accounts[account_number]

# Example usage
bank = Bank()
bank.create_account("123456", 1000)  # Create account with initial balance
bank.deposit("123456", 500)           # Deposit money
bank.withdraw("123456", 200)          # Withdraw money
print(f"Account balance: ${bank.get_balance('123456'):.2f}")  # Get current balance

# Uncommenting the following lines will raise errors
# bank.create_account("123456")         # Attempt to create an existing account
# bank.withdraw("123456", 1500)         # Attempt to withdraw more than the balance
