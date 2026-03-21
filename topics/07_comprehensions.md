# Comprehensions

## List
```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]

# Nested
flat = [n for row in [[1,2],[3,4]] for n in row]
```

## Dict
```python
squared  = {x: x**2 for x in range(5)}
inverted = {v: k for k, v in d.items()}
```

## Set
```python
unique_sq = {x**2 for x in [-2,-1,0,1,2]}
```

## Generator (lazy)
```python
gen = (x**2 for x in range(1000000))
next(gen)   # consume one at a time
sum(gen)    # or consume all
```

## When to use what
- **List comp** → need a list, moderate data
- **Generator** → large data, single pass
- **Dict comp** → transform or invert a dict
- **Set comp** → deduplicate + transform
