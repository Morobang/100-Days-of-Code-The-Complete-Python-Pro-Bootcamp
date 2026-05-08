# Day 48: Project — Caesar Cipher

**Phase:** 3 — Functions
**Difficulty:** ⭐⭐⭐

## Project description

Build a Caesar cipher encoder and decoder. A Caesar cipher shifts each letter in the alphabet by a fixed number of positions. For example, with a shift of 3: `A → D`, `B → E`, `Z → C` (wraps around). Non-letter characters pass through unchanged.

## Requirements

- `encode(text, shift)` — shifts each letter forward by `shift` positions
- `decode(text, shift)` — reverses the encoding
- Preserve case: uppercase stays uppercase, lowercase stays lowercase
- Non-letter characters (spaces, punctuation, digits) pass through unchanged
- Menu options: encode, decode, quit

## Example session

```
=== Caesar Cipher ===
1. Encode
2. Decode
3. Quit

Choice: 1
Text: Hello, World!
Shift: 3
Encoded: Khoor, Zruog!

Choice: 2
Text: Khoor, Zruog!
Shift: 3
Decoded: Hello, World!

Choice: 3
Goodbye!
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Skeleton with TODO comments |
| `solution/caesar_cipher.py` | Complete solution |

## Concepts used
Days 1–47 — functions, loops, strings, `ord()`, `chr()`, `isalpha()`, `isupper()`
