# Day 9 — Quick Reference

## Case methods

```python
'hello'.upper()         # 'HELLO'
'HELLO'.lower()         # 'hello'
'hello world'.title()   # 'Hello World'
'Hello'.swapcase()      # 'hELLO'
```

## Whitespace

```python
'  hello  '.strip()     # 'hello'
'  hello  '.lstrip()    # 'hello  '
'  hello  '.rstrip()    # '  hello'
```

## Searching

```python
'banana'.count('a')          # 3
'banana'.find('n')           # 2  — index of first match
'banana'.find('z')           # -1 — not found
'hello'.startswith('he')     # True
'hello'.endswith('lo')       # True
```

## Modifying

```python
'hello world'.replace('world', 'Python')  # 'hello Python'
```

## Split and join

```python
'a,b,c'.split(',')           # ['a', 'b', 'c']
'hello world'.split()        # ['hello', 'world']  — splits on whitespace
' | '.join(['a', 'b', 'c'])  # 'a | b | c'
```

## Checking

```python
'123'.isdigit()     # True  — all digits
'12.3'.isdigit()    # False — '.' is not a digit
'abc'.isalpha()     # True  — all letters
'abc1'.isalnum()    # True  — letters and digits only
'   '.isspace()     # True  — all whitespace
```

## Gotchas

- Methods return a **new** string — the original is never changed.
- `.find()` returns `-1` when not found (not an error).
- `'12.3'.isdigit()` is `False` — the dot is not a digit.
- Methods are case-sensitive: `'Hello'.startswith('hello')` is `False`.
- Chain methods: `'  HELLO  '.strip().lower()` → `'hello'`
