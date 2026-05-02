# Mad Libs Generator — Solution
# Day 7 Project

print("=== MAD LIBS GENERATOR ===")
print("Answer the questions. Don't think too hard — random is better!")
print()

# Collect words
person_name = input("Enter a person's name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective (describing word): ")
verb = input("Enter a verb (action word, e.g. 'run'): ")
animal = input("Enter an animal: ")
number = input("Enter a number: ")
food = input("Enter a type of food: ")

# Build and print the story
print()
print("--- YOUR STORY ---")
print()

story = (
    person_name + " walked into the " + place + " wearing a " + adjective + " hat.\n"
    "The plan was simple: " + verb + " as fast as possible and grab some " + food + ".\n"
    "Nobody expected the " + number + " " + animal + "s waiting by the entrance.\n"
    "\"I have everything under control,\" said " + person_name + ".\n"
    "The " + animal + "s disagreed."
)

print(story)

print()
print("-" * 40)
print("Thanks for playing!")
