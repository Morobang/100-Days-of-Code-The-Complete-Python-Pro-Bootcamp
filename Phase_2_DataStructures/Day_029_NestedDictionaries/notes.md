# Day 29 — Quick Reference: Nested Dictionaries

## Structure
```python
data = {
    'outer_key': {
        'inner_key': value,
        ...
    },
    ...
}
```

## Accessing
```python
data['outer']['inner']                        # direct — KeyError if missing
data.get('outer', {}).get('inner', default)   # safe — no KeyError
inner = data['outer']                         # store inner dict for readability
inner['key']
```

## Modifying
```python
data['outer']['inner'] = new_value     # update existing nested value
data['outer']['new_key'] = value       # add new key to inner dict
data['new_outer'] = {'key': value}     # add whole new outer entry
```

## Iterating
```python
for outer_key, inner_dict in data.items():
    for field, value in inner_dict.items():
        print(field, value)
```

## Aggregating across nested dicts
```python
total = 0
for info in data.values():
    total += info['score']
average = total / len(data)
```

## Finding best/worst by a nested field
```python
best = None
best_val = -1
for name, info in data.items():
    if info['score'] > best_val:
        best_val = info['score']
        best = name
```
