#Create a Python class for a "Bank" that manages multiple bank accounts. 
#Implement methods to add accounts, deposit money, withdraw money, and display account balances.

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with initial balance of ${initial_balance}")
        else:
            print(f"Account {account_number} already exists")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} into account {account_number}")
        else:
            print(f"Account {account_number} does not exist")
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                print(f"Withdrawn ${amount} from account {account_number}")
            else:
                print(f"Insufficient funds in account {account_number}")
        else:
            print(f"Account {account_number} does not exist")
    
    def display_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: ${self.accounts[account_number]}")
        else:
            print(f"Account {account_number} does not exist")

# Example usage
bank = Bank()

bank.add_account("123456789", 1000)
bank.add_account("987654321", 500)
bank.add_account("123456789")  # Trying to add an existing account
print()

bank.deposit("123456789", 500)
bank.deposit("987654321", 1000)
bank.deposit("111111111", 200)  # Trying to deposit into a non-existing account
print()

bank.withdraw("123456789", 200)
bank.withdraw("987654321", 1500)  # Trying to withdraw more than the balance
bank.withdraw("111111111", 100)  # Trying to withdraw from a non-existing account
print()

bank.display_balance("123456789")
bank.display_balance("987654321")
bank.display_balance("111111111")  # Trying to display balance of a non-existing account