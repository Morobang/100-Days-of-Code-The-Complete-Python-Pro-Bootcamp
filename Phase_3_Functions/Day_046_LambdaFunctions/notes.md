# Lambda Functions — Quick Reference

## Syntax
```python
lambda parameters: expression
```
- Returns the value of `expression` — no `return` keyword needed
- Only a **single expression** (no `if` blocks, no loops, no assignments)
- Anonymous — has no name unless you assign it to a variable

## Basic Examples
```python
double = lambda x: x * 2
print(double(5))      # 10

add = lambda x, y: x + y
print(add(3, 7))      # 10

greet = lambda name: f'Hello, {name}!'
print(greet('Alice')) # Hello, Alice!
```

## Most Common Use: `key=` in Sorting
```python
words = ['banana', 'apple', 'cherry', 'date']

# sort by length
sorted(words, key=lambda w: len(w))
# ['date', 'apple', 'banana', 'cherry']

# sort descending
sorted(words, key=lambda w: len(w), reverse=True)
# ['banana', 'cherry', 'apple', 'date']
```

## Sorting Lists of Dicts
```python
people = [{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}]
sorted(people, key=lambda p: p['age'])   # Alice first
```

## Sorting Lists of Tuples
```python
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted(pairs, key=lambda t: t[1])        # sort by second element
# [(3, 'a'), (1, 'b'), (2, 'c')]
```

## lambda vs def

| Use `lambda` | Use `def` |
|-------------|-----------|
| Short, one-line, used inline as `key=` | More than one line |
| Only an expression | Needs a docstring or comment |
| Throwaway — assigned to no name | The function has a meaningful name |

## What lambda Can't Do
```python
# No statements (if blocks, loops, assignments):
bad = lambda x: if x > 0: x else -x  # SyntaxError

# Use def instead:
def abs_val(x):
    if x > 0:
        return x
    return -x
```
