# Day 1 — Quick Reference

## print() syntax

```python
print(value)                        # print one value
print(value1, value2, value3)       # print multiple values (separated by space by default)
print(value1, value2, sep="-")      # custom separator
print(value, end="")                # custom ending (default is \n)
print()                             # prints a blank line
```

## Escape sequences

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab (indent) |
| `\\` | Literal backslash |
| `\"` | Literal double quote inside a string |
| `\'` | Literal single quote inside a string |

## f-strings (preview)

```python
name = "Alex"
print(f"Hello, {name}!")   # Hello, Alex!
```

## Gotchas

- `print()` with no arguments prints a blank line — it doesn't error
- `sep` and `end` are keyword arguments — they must be named, e.g. `sep="-"` not just `"-"`
- The default `end` is `"\n"` (a newline) — that's why each print goes on its own line

## Interview tip

- `print()` is a function — it has parentheses. In Python 2 it was a statement (`print "hello"`). If you ever see that syntax, it's old Python 2 code.
