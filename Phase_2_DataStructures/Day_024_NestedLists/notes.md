# Day 24 — Quick Reference: Nested Lists

## Creating a 2D list
```python
grid = [
    [1, 2, 3],   # row 0
    [4, 5, 6],   # row 1
    [7, 8, 9]    # row 2
]
```

## Accessing elements
```python
grid[row][col]      # element at row, col
grid[0]             # entire first row
grid[-1][-1]        # last element (bottom-right)
```

## Dimensions
```python
len(grid)      # number of rows
len(grid[0])   # number of columns
```

## Modifying elements
```python
grid[1][2] = 99   # set row 1, col 2 to 99
```

## Iterating — all elements
```python
for row in grid:
    for value in row:
        print(value, end=' ')
    print()   # newline after each row
```

## Iterating — with indices
```python
for r, row in enumerate(grid):
    for c, value in enumerate(row):
        print(f'[{r}][{c}] = {value}')
```

## Building a 2D list with loops
```python
grid = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)
    grid.append(row)
```

## Extracting a column
```python
col = []
for row in grid:
    col.append(row[col_index])
```
