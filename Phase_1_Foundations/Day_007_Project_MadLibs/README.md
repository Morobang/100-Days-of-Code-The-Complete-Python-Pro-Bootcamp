# Day 7 — Project: Mad Libs Generator

Time to build something. Today you use everything from Days 1–6 to create a complete interactive program.

## What is this project?

A Mad Libs generator asks the user for random words — a name, a verb, an adjective — then plugs them into a story template. The result is usually funny and nonsensical. The user does not see the story until all the words have been collected.

## What you will use

- `print()` — Days 1
- Variables — Day 2
- String concatenation — Day 3
- `input()` — Day 6
- f-strings (optional, preview from Day 1) — for building the story

## Requirements

Your program must:

1. Ask the user for at least **6 different words** — mix of names, places, adjectives, verbs, nouns, and numbers
2. Store each word in a clearly named variable
3. Use those variables to build a complete story
4. Print the full story at the end
5. The story must make grammatical sense as a template — it should be funny when random words are inserted

## Example run

```
=== MAD LIBS GENERATOR ===
Answer the questions below. Don't think too hard — random is better!

Enter a person's name: Bob
Enter a place: supermarket
Enter an adjective (describing word): purple
Enter a verb (action word): sprint
Enter an animal: penguin
Enter a number: 47

--- YOUR STORY ---
Bob walked into the supermarket wearing a purple hat.
As soon as he arrived, he decided to sprint past the fruit section.
Everyone stopped and stared at the 47 penguins following close behind.
"This is completely normal," said Bob, and nobody disagreed.
```

## Stretch goals (optional)

- Ask for more words and write a longer story
- Print the story title in ALL CAPS using a string method you remember from the notes
- Let the user enter their own name and use it as the narrator

## When you are done

Compare your solution to `solution/mad_libs.py`. There is no single right answer — the story is yours.
