# Day 06 — Control Flow — SOLUTIONS

def grade(score):
    if score >= 90:   return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else:             return 'F'

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def rps(player, computer):
    if player == computer: return 'Draw'
    wins = {'rock':'scissors','paper':'rock','scissors':'paper'}
    return 'Win' if wins[player] == computer else 'Lose'
