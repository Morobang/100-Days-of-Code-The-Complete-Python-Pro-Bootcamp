# Day 43 Solutions

# Challenge 1
greeting = 'Hello, world!'

def say_hello():
    print(greeting)

say_hello()

print()

# Challenge 2
total = 100

def add_bonus(total, bonus):
    total = total + bonus
    print(f'New total: {total}')
    return total

total = add_bonus(total, 50)

print()

# Challenge 3
calls = 0

def count_calls():
    global calls
    calls += 1

count_calls()
count_calls()
count_calls()
print(calls)  # 3

print()

# Challenge 4
value = 'global'

def outer():
    value = 'enclosing'

    def inner():
        print(value)  # enclosing — no local, finds enclosing

    inner()

outer()
print(value)  # global — outer() never touched the global

print()

# Challenge 5
def add_entry(history, entry):
    history.append(entry)
    return history

history = []
history = add_entry(history, 'first')
history = add_entry(history, 'second')
print(history)
