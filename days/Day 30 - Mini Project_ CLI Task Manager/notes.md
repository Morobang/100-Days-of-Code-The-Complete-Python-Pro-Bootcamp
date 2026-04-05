# Day 30 — Mini Project: CLI Task Manager

## What this practises
- OOP: Task class with from_dict/to_dict pattern
- JSON persistence: save/load on every change
- File I/O: FileNotFoundError handled gracefully
- Error handling: bad input never crashes the app
- Sorting: by priority using a custom key
- CLI loop: while True + break pattern

## Build checklist
- [ ] Task class with all methods + __str__
- [ ] TaskManager loads on startup
- [ ] Saves after every change
- [ ] List sorted by priority descending
- [ ] Complete and delete work correctly
- [ ] Main loop handles all inputs gracefully

## Stretch goals
- [ ] Add task ID (UUID) so you can reference by ID not title
- [ ] Export tasks as CSV
- [ ] Due date warnings (overdue tasks shown in red)
- [ ] Undo last action
