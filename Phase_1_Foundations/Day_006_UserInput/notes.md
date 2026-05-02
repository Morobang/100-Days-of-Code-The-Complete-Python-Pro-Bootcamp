# Day 6 — Quick Reference

## input() syntax

```python
name = input("Enter your name: ")    # prompt is optional but helpful
number = input("Enter a number: ")   # returns a string even if user types 42
```

## Converting input to numbers

```python
age = int(input("Enter your age: "))         # convert to integer
price = float(input("Enter the price: "))    # convert to float
```

## Common pattern

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old.")
```

## Gotchas

- `input()` **always** returns a string. `int("25")` works. `int(input(...))` works. But `"25" + 5` will error — you must convert first.
- Leave a space before the closing quote in your prompt: `"Enter name: "` not `"Enter name:"` — otherwise the cursor appears right after the colon with no breathing room.
- If you try to convert something that isn't a valid number (e.g. user types "hello" when you call `int(input(...))`), you get a `ValueError`. You'll learn to handle this on Day 54.
