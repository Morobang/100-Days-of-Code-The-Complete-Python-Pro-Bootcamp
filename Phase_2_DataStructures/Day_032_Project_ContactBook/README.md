# Day 32: Project — Contact Book

**Phase:** 2 — Data Structures
**Difficulty:** ⭐⭐⭐

## Project description

Build an interactive contact book that stores contacts as a nested dictionary (name → {phone, email}). The user can add, view, search, update, delete, and quit.

## Requirements

- **Add** — store a new contact; reject if name already exists
- **View all** — print every contact in alphabetical order
- **Search** — look up a contact by name (case-insensitive); show all their details
- **Update** — change the phone or email for an existing contact
- **Delete** — remove a contact by name
- **Quit** — exit

## Example session

```
=== Contact Book ===
1. Add contact
2. View all
3. Search
4. Update
5. Delete
6. Quit

Choice: 1
Name: Alice
Phone: 083-111-2222
Email: alice@mail.com
Contact 'Alice' added.

Choice: 2
Alice  | 083-111-2222 | alice@mail.com

Choice: 3
Search: alice
Alice  | 083-111-2222 | alice@mail.com

Choice: 5
Delete: Alice
'Alice' deleted.
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Skeleton with TODO comments — start here |
| `solution/contact_book.py` | Complete solution |

## Concepts used
Days 1–31 — nested dicts, loops, string methods, dict methods
