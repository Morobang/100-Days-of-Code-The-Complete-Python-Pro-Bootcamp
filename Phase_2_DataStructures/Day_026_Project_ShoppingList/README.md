# Day 26: Project — Shopping List

**Phase:** 2 — Data Structures
**Difficulty:** ⭐⭐⭐

## Project description

Build an interactive shopping list manager. The user can add items, remove items, view the current list, and quit. The program runs in a loop until the user exits.

## Requirements

- Display a menu on each loop iteration
- **Add** — append an item to the list (reject blank input)
- **Remove** — remove an item by name; handle the case where it's not in the list
- **View** — print all items, numbered; print a message if the list is empty
- **Quit** — exit the loop

## Example session

```
=== Shopping List ===
1. Add item
2. Remove item
3. View list
4. Quit
Choice: 3
Your list is empty.

Choice: 1
Item to add: Milk
'Milk' added.

Choice: 1
Item to add: Eggs
'Eggs' added.

Choice: 3
1. Milk
2. Eggs

Choice: 2
Item to remove: Milk
'Milk' removed.

Choice: 4
Goodbye!
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Skeleton with TODO comments — start here |
| `solution/shopping_list.py` | Complete solution |

## Concepts used
Days 1–25 — lists, loops, conditionals, string methods, f-strings
