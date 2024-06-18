# Implement a base class "BankAccount" with methods for deposit and withdraw. 
# Create a derived class "SavingsAccount" that inherits from "BankAccount" 
# and adds an interest calculation method.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        self.display_balance()
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
            self.display_balance()
        else:
            print("Insufficient balance.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest Calculated: ${interest}")
        self.display_balance()

# Example usage
account = BankAccount("1234567890")
account.deposit(1000)
account.withdraw(500)
account.withdraw(1000)

savings_account = SavingsAccount("9876543210", 1000, 0.05)
savings_account.deposit(500)
savings_account.calculate_interest()