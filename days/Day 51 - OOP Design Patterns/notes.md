# Day 51 — OOP Design Patterns

## The Gang of Four patterns
| Pattern | Category | Use when |
|---------|----------|---------|
| Singleton | Creational | Only one instance needed |
| Factory | Creational | Object creation logic varies |
| Builder | Creational | Complex object construction |
| Observer | Behavioural | Many objects react to one |
| Strategy | Behavioural | Swap algorithms at runtime |
| Command | Behavioural | Undo/redo, logging actions |
| Decorator | Structural | Add features without subclassing |
| Adapter | Structural | Incompatible interfaces |

## Gotchas
- Singleton can cause issues in testing — hard to mock
- Prefer composition over inheritance (Decorator pattern)
- Strategy and Command are excellent for open/closed principle

## Interview tips
- "How would you design X?" → reach for a pattern
- Factory → when you have `if type == 'A': return A()`
- Observer → event systems, pub/sub
- Command → undo history, task queues
