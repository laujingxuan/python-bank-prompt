class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True
    
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def getBalance(self):
        return self.balance