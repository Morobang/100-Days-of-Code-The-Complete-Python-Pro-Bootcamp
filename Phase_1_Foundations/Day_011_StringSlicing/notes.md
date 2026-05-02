# Day 11 — Quick Reference

## Indexing review

```python
s = 'Python'
s[0]     # 'P'   — first character
s[-1]    # 'n'   — last character
s[-2]    # 'o'   — second from end
```

## Slicing syntax

```python
s[start:stop]          # from start up to (not including) stop
s[start:stop:step]     # every step-th character
s[:stop]               # from the beginning up to stop
s[start:]              # from start to the end
s[:]                   # full copy of the string
```

## Examples

```python
s = 'Python'
s[0:3]    # 'Pyt'    — indices 0, 1, 2
s[2:5]    # 'tho'    — indices 2, 3, 4
s[:3]     # 'Pyt'    — from start
s[3:]     # 'hon'    — to end
s[::2]    # 'Pto'    — every 2nd character
s[::-1]   # 'nohtyP' — reversed
```

## Negative indices in slices

```python
s = 'Python'
s[-3:]    # 'hon'    — last 3 characters
s[:-3]    # 'Pyt'    — everything except last 3
s[-4:-1]  # 'tho'    — from 4th-from-end to 2nd-from-end
```

## Reversing

```python
'hello'[::-1]   # 'olleh'
```

## Gotchas

- `stop` is **exclusive** — `s[0:3]` gives indices 0, 1, 2 (not 3).
- Out-of-range stop never crashes: `s[0:100]` on a 6-char string gives the full string.
- Step of `-1` walks backwards. Omit start/stop for a full reverse: `s[::-1]`.
- Slicing returns a new string — the original is unchanged.
