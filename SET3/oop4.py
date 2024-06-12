# Create a Python class for a "BankAccount" with methods to deposit and withdraw money. 
# Implement a method to display the account balance.


class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount} from account {self.account_number}")
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

# Example usage
account1 = BankAccount("123456789", 1000)
account2 = BankAccount("987654321")

account1.display_balance()
account2.display_balance()
print()

account1.deposit(500)
account2.deposit(1000)
print()

account1.withdraw(200)
account2.withdraw(1500)
print()

account1.display_balance()
account2.display_balance()