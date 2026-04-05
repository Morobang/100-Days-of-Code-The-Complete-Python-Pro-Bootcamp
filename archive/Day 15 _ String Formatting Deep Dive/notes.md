# Day 15 — String Formatting Deep Dive

## Key syntax
```python
# Format spec: {value:[[fill]align][width][.precision][type]}
f'{3.14:.2f}'        # 3.14       — 2 decimal places
f'{3.14:10.2f}'      # '      3.14' — right-align in width 10
f'{42:<10}'          # '42        ' — left align
f'{42:>10}'          # '        42' — right align
f'{42:^10}'          # '    42    ' — centre
f'{42:0>10}'         # '0000000042' — zero-fill
f'{1000:,}'          # '1,000'     — comma separator
f'{0.75:.1%}'        # '75.0%'     — percentage
f'{255:b}'           # '11111111'  — binary
f'{255:x}'           # 'ff'        — hex

# Repeating a character
'-' * 30              # '-----...'
```

## Gotchas
- `f'{value:}'` — the colon separates value from format spec
- Width is MINIMUM width — won't truncate if value is longer
- `.2f` rounds for display only — the actual float is unchanged

## Interview tips
- Clean output = professional code — formatting matters in data engineering
- Know how to align columns for tabular output
- `f'{value:,}'` for large numbers is immediately readable
