# Define a base class "BankAccount" with methods for deposit and withdraw. Create derived classes "SavingsAccount" and "CheckingAccount" that implement the methods differently.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def withdraw(self, amount):
        if self.balance - amount >= 100:  # Minimum balance requirement
            return super().withdraw(amount)
        return False


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return True
        return False


# Usage example
if __name__ == "__main__":
    # Create a savings account
    savings = SavingsAccount("SA001", 1000, 0.05)
    print(f"Savings account balance: ${savings.get_balance()}")

    # Deposit to savings account
    savings.deposit(500)
    print(f"After deposit: ${savings.get_balance()}")

    # Apply interest
    interest_earned = savings.apply_interest()
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"After applying interest: ${savings.get_balance()}")

    # Try to withdraw more than minimum balance
    if savings.withdraw(1500):
        print("Withdrawal successful")
    else:
        print("Withdrawal failed: Minimum balance not maintained")

    # Create a checking account
    checking = CheckingAccount("CA001", 500, 200)
    print(f"\nChecking account balance: ${checking.get_balance()}")

    # Withdraw within overdraft limit
    if checking.withdraw(600):
        print("Withdrawal successful")
        print(f"New balance: ${checking.get_balance()}")
    else:
        print("Withdrawal failed")

    # Try to withdraw beyond overdraft limit
    if checking.withdraw(200):
        print("Withdrawal successful")
    else:
        print("Withdrawal failed: Exceeds overdraft limit")