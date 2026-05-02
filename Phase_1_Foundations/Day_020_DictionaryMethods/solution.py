# Day 20 — Solutions

# Challenge 1: .get() with a default
inventory = {"apple": 50, "banana": 30, "cherry": 20}
item = input("Enter an item name: ").lower().strip()
count = inventory.get(item, 0)
if count > 0:
    print(f"{item}: {count} in stock")
else:
    print(f"{item}: not in inventory")

# Challenge 2: .keys(), .values(), .items()
scores = {"Alice": 88, "Bob": 75, "Charlie": 92}
print("Names: ", list(scores.keys()))
print("Scores:", list(scores.values()))
print("---")
for name, score in scores.items():
    print(f"  {name:<10} {score}")

# Challenge 3: .update() to merge
defaults = {"theme": "light", "language": "english", "font_size": 14}
user_prefs = {"theme": "dark", "font_size": 16}
print("Before:", defaults)
defaults.update(user_prefs)
print("After: ", defaults)

# Challenge 4: .pop() to remove a key
scores = {"Alice": 88, "Bob": 75, "Charlie": 92}
removed = scores.pop("Bob")
print(f"Removed Bob with score: {removed}")
print("Remaining:", scores)

# Challenge 5: Contact book
contacts = {}
print("Add contacts — type 'done' as name to stop.")
while True:
    name = input("Name: ").strip()
    if name.lower() == "done":
        break
    phone = input("Phone: ").strip()
    contacts[name] = phone
    print(f"  '{name}' saved.")

lookup = input("\nLook up a contact: ").strip()
result = contacts.get(lookup, "Not found")
print(f"{lookup}: {result}")
