# Day 16 — Quick Reference

## Creating lists

```python
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'hello', True, 3.14]
empty = []
```

## Indexing

```python
fruits = ['apple', 'banana', 'cherry']
fruits[0]     # 'apple'   — first item
fruits[2]     # 'cherry'  — last item
fruits[-1]    # 'cherry'  — last item (negative index)
fruits[-2]    # 'banana'  — second from end
```

## Slicing

```python
fruits = ['apple', 'banana', 'cherry', 'mango']
fruits[1:3]   # ['banana', 'cherry']  — same rules as string slicing
fruits[:2]    # ['apple', 'banana']
fruits[2:]    # ['cherry', 'mango']
```

## len()

```python
len([1, 2, 3])    # 3
len([])           # 0
```

## Modifying items

```python
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'    # ['apple', 'blueberry', 'cherry']
```

## append() and remove()

```python
fruits = ['apple', 'banana']
fruits.append('cherry')    # ['apple', 'banana', 'cherry']  — adds to end
fruits.remove('banana')    # ['apple', 'cherry']  — removes first match
```

## in operator

```python
'apple' in ['apple', 'banana']    # True
'mango' in ['apple', 'banana']    # False
```

## Iterating

```python
for item in ['a', 'b', 'c']:
    print(item)
```

## Gotchas

- Indexing starts at `0`, not `1`.
- `list[-1]` is the last item — very handy.
- `append()` adds to the **end**. To add elsewhere, use `.insert()` (Day 17).
- `remove()` removes the **first** occurrence. It raises an error if the item is not found.
- Lists are **mutable** — you can change them after creation. Strings are not.
