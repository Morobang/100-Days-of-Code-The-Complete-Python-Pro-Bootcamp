# Day 22 Solutions

# Challenge 1
foods = ['pizza', 'pasta', 'sushi', 'tacos', 'curry']
print(foods[0])
print(foods[-1])
print(foods[len(foods) // 2])

# Challenge 2
evens = list(range(2, 21, 2))
countdown = list(range(10, 0, -1))
threes = list(range(3, 31, 3))
print(evens)
print(countdown)
print(threes)

# Challenge 3
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters[:4])
print(letters[-3:])
print(letters[::2])
print(letters[::-1])

# Challenge 4
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi', 'grape']
entry = input('Enter a fruit: ').lower()
if entry in fruits:
    print(f'We have {len(fruits)} fruits.')
    print(f'{entry} is at index {fruits.index(entry)}.')
else:
    print(f'{entry} is not available.')

# Challenge 5 — Part A explanation:
# team_b = team_a does not copy the list.
# Both names point to the same object in memory,
# so any change through either name affects the same list.

# Part B — fixed
team_a = ['Alice', 'Bob', 'Charlie']
team_b = team_a.copy()    # independent copy
team_b.append('Diana')
team_a.append('Eve')
print('team_a:', team_a)  # ['Alice', 'Bob', 'Charlie', 'Eve']
print('team_b:', team_b)  # ['Alice', 'Bob', 'Charlie', 'Diana']
