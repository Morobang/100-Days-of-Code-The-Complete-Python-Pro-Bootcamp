# Day 06 — Control Flow — SOLUTIONS

# Exercise 1 — grade calculator
def grade(score):
    if score >= 90:   return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else:             return 'F'

# Exercise 2 — leap year
def is_leap(year):
    # Divisible by 4, EXCEPT centuries unless also divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Exercise 3 — rock paper scissors
def rps(user, computer='rock'):
    if user == computer:
        return "Draw"
    wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    return "You win!" if wins[user] == computer else "Computer wins!"
