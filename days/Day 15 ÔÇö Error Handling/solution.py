# Day 15 — Error Handling — SOLUTIONS

def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0: raise ValueError("Must be positive")
            return val
        except ValueError as e:
            print(f"Invalid: {e}. Try again.")

def safe_get(d, key, default=None):
    try:
        return d[key]
    except (KeyError, TypeError):
        return default

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, bal=0):
        self.owner = owner
        self._bal  = bal

    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        self._bal += amount

    def withdraw(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        if amount > self._bal: raise InsufficientFundsError(f"Balance R{self._bal}, requested R{amount}")
        self._bal -= amount

    def balance(self): return self._bal
