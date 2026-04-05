# Day 76 — OOP Design Problems

## Design approach
```
1. Clarify requirements (ask questions)
2. Identify entities (nouns → classes)
3. Define relationships (has-a vs is-a)
4. Sketch class diagram
5. Start with core classes, add features
6. Apply SOLID principles
```

## Common OOP interview questions
- Parking lot, library system, hotel booking
- Card game (Blackjack, Chess)
- Elevator system
- Movie ticket booking
- File system

## Key design choices
| Choice | When |
|--------|------|
| Inheritance | "is-a" relationship |
| Composition | "has-a" relationship |
| Abstract class | Shared behaviour, can't instantiate |
| Interface/Protocol | Defines contract only |
| Enum | Fixed set of constants |
| Dataclass | Data container, auto __init__/__repr__ |

## Interview tips
- Think aloud — explain classes and why
- Start simple, evolve the design
- Mention trade-offs (e.g. "I used composition here because...")
- Use enums for states and types
