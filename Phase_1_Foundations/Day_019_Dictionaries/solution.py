# Day 19 — Solutions

# Challenge 1: Dictionary basics
person = {"name": "Alice", "age": 30, "city": "Cape Town"}
print(person["name"])
print(person["age"])
print(person["city"])

# Challenge 2: Add and update keys
person["email"] = "alice@example.com"
person["age"] = 31
print(person)

# Challenge 3: Capital city lookup
capitals = {
    "south africa": "Pretoria",
    "france": "Paris",
    "japan": "Tokyo",
    "brazil": "Brasilia",
    "germany": "Berlin",
    "australia": "Canberra",
}
country = input("Enter a country: ").lower().strip()
if country in capitals:
    print(f"The capital of {country.title()} is {capitals[country]}.")
else:
    print(f"Sorry, {country.title()} is not in the list.")

# Challenge 4: Iterate over dictionary
scores = {"Alice": 88, "Bob": 75, "Charlie": 92, "Diana": 81}
for name, score in scores.items():
    print(f"{name:<10} {score}")

# Challenge 5: Word frequency counter
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
for word, count in frequency.items():
    print(f"'{word}': {count}")
