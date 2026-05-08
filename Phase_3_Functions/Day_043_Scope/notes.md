# Scope — Quick Reference

## LEGB Rule
Python searches for names in this order:

| Letter | Scope | Where |
|--------|-------|-------|
| **L** | Local | Inside the current function |
| **E** | Enclosing | Outer function (nested functions only) |
| **G** | Global | Module level (top of file) |
| **B** | Built-in | Python's built-ins: `len`, `print`, `range`, … |

Python stops at the **first match** it finds.

---

## Local Scope
Variables assigned inside a function are local — invisible outside it.
```python
def f():
    x = 10   # local — only visible inside f
```

## Global Scope
Variables at module level. **Readable** inside functions with no keyword.
```python
name = 'Alice'       # global

def greet():
    print(name)      # reading global — fine, no keyword needed
```

## `global` Keyword
Required only when you want to **reassign** a global variable inside a function.
```python
count = 0

def increment():
    global count     # declare intent to modify the global
    count += 1
```
Without `global`, Python assumes `count += 1` is a local variable and raises `UnboundLocalError`.

## Mutable Globals — No Keyword Needed
**Mutating** (`.append()`, `.update()`, etc.) doesn't reassign the name — no `global` needed.
```python
items = []

def add(item):
    items.append(item)   # mutation, not reassignment — no global keyword
```

## Why `global` Is Usually a Code Smell
- Creates hidden dependency between a function and module-level state
- Makes functions hard to test and reason about
- **Prefer:** pass the value as a parameter and return the new value

```python
# instead of global:
def increment(count):
    return count + 1

count = 0
count = increment(count)
```
