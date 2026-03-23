# Day 06 — Control Flow

## Key syntax
```python
if x > 0:       ...
elif x < 0:     ...
else:           ...

# Ternary
label = "yes" if condition else "no"

# Operators
==  !=  >  <  >=  <=
and   or   not
x in [1,2,3]
x not in [1,2,3]
```

## Gotchas
- `=` assigns, `==` compares — very common mistake
- `elif` stops at the FIRST True — order matters
- Indentation defines the block — it's not optional

## Interview tips
- FizzBuzz: check `%15` FIRST, then `%3`, then `%5`
- Leap year rule is a classic condition test
- "Replace if-elif with a dict" is a common refactor question
