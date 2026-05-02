# Day 9 — Solutions

# Challenge 1: Name in UPPER and lower
name = input("Enter your name: ")
print(name.upper())
print(name.lower())

# Challenge 2: Count occurrences of 'a' (case-insensitive)
word = input("Enter a word: ")
count = word.lower().count("a")
print(f"The letter 'a' appears {count} time(s)")

# Challenge 3: Strip whitespace, replace spaces with hyphens
text = input("Enter some text (spaces are fine): ")
cleaned = text.strip().replace(" ", "-")
print(cleaned)

# Challenge 4: Split CSV, print each item, join with " and "
items = input("Enter 3 items separated by commas: ")
parts = items.split(",")
print(parts[0].strip())
print(parts[1].strip())
print(parts[2].strip())
joined = " and ".join(parts)
print(joined)

# Challenge 5: Inspect a word's properties
word = input("Enter any word: ")
print("All digits?     ", word.isdigit())
print("All letters?    ", word.isalpha())
print("Starts with 'a'?", word.lower().startswith("a"))
print("Ends with 'ing'?", word.lower().endswith("ing"))
print("Uppercase:      ", word.upper())
