# Create an Account class with acno, customer name, balance with all required methods   

class Account:
    def __init__(self, acno, customer_name, balance=0):
        self.acno = acno
        self.customer = customer_name
        self.current_balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.current_balance += amount
        return True

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.current_balance:
            raise ValueError("Insufficient balance.")
        self.current_balance -= amount
        return True

    def get_balance(self):
        """Get the current balance of the account."""
        return self.current_balance

    def __str__(self):
        return f"Account Number: {self.acno}, Customer Name: {self.customer}, Balance: {self.current_balance}"


a = Account(12345, "John Doe", 1000)

try:
    a.withdraw(10000)
except ValueError as e:
    print(f"Error: {e}")
