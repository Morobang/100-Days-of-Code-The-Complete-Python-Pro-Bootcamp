# Day 2 — Quick Reference

## Creating a variable

```python
name = "Alex"     # string
age = 25          # integer
height = 1.75     # float
is_student = True # boolean
```

## Naming rules (enforced by Python)

| Rule | Example |
|------|---------|
| Letters, digits, underscores only | `user_name`, `age2` |
| Cannot start with a digit | `2name` — INVALID |
| Cannot be a keyword | `if`, `for`, `class` — INVALID |
| Case-sensitive | `name` and `Name` are different variables |

## Naming convention (snake_case)

```python
# Good
first_name = "Alex"
total_price = 99.99
is_logged_in = True

# Avoid
firstName = "Alex"    # camelCase — works but not Python style
FirstName = "Alex"    # PascalCase — reserved for classes (Day 57)
```

## Checking the type of a variable

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hello")   # <class 'str'>
type(True)      # <class 'bool'>
```

## Reassigning

```python
score = 0
score = 100     # score is now 100 — the old value is gone
```

## Gotchas

- `=` means "assign", not "equals". `==` means "equals" (you'll see this on Day 12).
- Variable names are case-sensitive: `Name` and `name` are two different variables.
- You can't use Python keywords as variable names: `for`, `if`, `while`, `class`, `True`, `False`, `None` are all off-limits.
