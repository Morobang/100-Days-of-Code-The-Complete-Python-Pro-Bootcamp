# Day 012 — __init__ & Instance Attributes — REFERENCE SOLUTION

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance        # _ prefix signals "internal"
        self._transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(("deposit", amount))

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance is R{self._balance:.2f}")
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))

    def get_balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f"BankAccount({self.owner}, R{self._balance:.2f})"
