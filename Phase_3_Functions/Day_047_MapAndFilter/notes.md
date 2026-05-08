# Map and Filter — Quick Reference

## map(func, iterable)
Applies `func` to every item. Returns an **iterator** — wrap with `list()`.
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))  # [2, 4, 6, 8]
```

## filter(func, iterable)
Keeps items where `func(item)` is truthy. Returns an **iterator**.
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]
```

## Both Return Iterators
```python
result = map(str, [1, 2, 3])
print(result)        # <map object at ...>
print(list(result))  # ['1', '2', '3']
```

## Using Named Functions
```python
def square(x):
    return x ** 2

squared = list(map(square, [1, 2, 3, 4]))  # [1, 4, 9, 16]
```

## Chaining map and filter
```python
nums = range(1, 11)
# squares of even numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
# [4, 16, 36, 64, 100]
```
Read inside-out: filter first, then map the result.

## map/filter vs List Comprehensions

| Operation | map / filter | List comprehension |
|-----------|-------------|-------------------|
| Transform every item | `list(map(f, it))` | `[f(x) for x in it]` |
| Filter items | `list(filter(p, it))` | `[x for x in it if p(x)]` |
| Transform + filter | `list(map(f, filter(p, it)))` | `[f(x) for x in it if p(x)]` |

List comprehensions are usually more readable in Python.
`map`/`filter` are worth knowing for reading other people's code.
