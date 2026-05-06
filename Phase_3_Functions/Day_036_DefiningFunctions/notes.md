# Day 36 — Quick Reference: Defining Functions

## Syntax
```python
def function_name():
    """Optional one-line docstring."""
    # body — runs every time the function is called
    print('something')

function_name()   # call it
```

## Rules
- `def` keyword starts the definition
- Name: lowercase, underscores, no spaces
- Empty `()` = no parameters (today's focus)
- `:` ends the header
- Body must be indented (4 spaces or 1 tab — be consistent)
- Calling: `name()` — the parentheses are required

## Docstrings
```python
def greet():
    """Print a greeting to the user."""
    print('Hello!')
```
- First string inside the body
- Use `help(function_name)` to read it

## Functions calling functions
```python
def header():
    print('=== Title ===')

def report():
    header()       # call another function
    print('body')

report()           # runs header() then print('body')
```

## Implicit None return
```python
def say_hi():
    print('Hi')

result = say_hi()  # result is None
```
Every function returns `None` if there is no `return` statement.
