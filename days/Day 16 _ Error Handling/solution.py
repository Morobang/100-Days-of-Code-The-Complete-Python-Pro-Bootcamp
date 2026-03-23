# Day 16 — Error Handling — SOLUTIONS

# Exercise 1
def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Must be positive")
            return value
        except ValueError as e:
            print(f"Invalid: {e}. Try again.")


# Exercise 2
def safe_get(d: dict, key, default=None):
    try:
        return d[key]
    except KeyError:
        return default
    # alternatively: return d.get(key, default)


# Exercise 3
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw R{amount} — balance is R{balance}")


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
