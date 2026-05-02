# Day 13 — Quick Reference

## Basic while loop

```python
while condition:
    # runs while condition is True
    # something must eventually make condition False, or you get an infinite loop
```

## Counting pattern

```python
# Count up
n = 1
while n <= 5:
    print(n)
    n += 1      # n = n + 1

# Count down
n = 5
while n >= 1:
    print(n)
    n -= 1      # n = n - 1
```

## break — exit immediately

```python
n = 1
while True:          # infinite loop
    print(n)
    n += 1
    if n > 5:
        break        # jumps out of the loop
```

## continue — skip to next iteration

```python
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)         # only prints odd numbers
```

## Accumulator pattern

```python
total = 0
count = 0
number = float(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    count += 1
    number = float(input("Enter a number (0 to stop): "))
print(f"Total: {total}, Count: {count}")
```

## Input validation

```python
age = int(input("Enter your age: "))
while age <= 0:
    print("Age must be positive.")
    age = int(input("Enter your age: "))
```

## Gotchas

- Always make sure the loop condition can eventually become `False` — otherwise the loop runs forever.
- `n += 1` is shorthand for `n = n + 1`. Forgetting this is the most common cause of infinite loops.
- `break` exits the entire loop. `continue` only skips the rest of the current iteration.
- The condition is checked **before** each iteration. If it's False from the start, the loop body never runs.
