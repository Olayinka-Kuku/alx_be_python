# bank_account.py

class BankAccount:
    def __init__ (self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw a specified amount from the account balance."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")