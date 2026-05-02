# Grade Checker — Day 14 Project
# --------------------------------------------------
# Build a program that takes a student name and score,
# validates the input, calculates a grade, and prints
# a neat result card.

# Step 1: Ask for the student's name
# Tip: use .strip().title() to clean and capitalise it
name = ...

# Step 2: Ask for the score
# Convert it to an integer
score = ...

# Step 3: Validate the score
# Keep asking until the score is between 0 and 100 (inclusive)
while ...:
    print("Score must be between 0 and 100. Try again.")
    score = ...

# Step 4: Calculate the letter grade
# A: 90+, B: 80+, C: 70+, D: 60+, F: below 60
# Tip: use if / elif / else. Once a condition matches, the rest are skipped.
grade = ...

# Step 5: Determine pass or fail
# Passing score is 60 or above
if ...:
    result = "Pass"
else:
    result = "Fail"

# Step 6: Print the result card
# Use "=" * 30 for the border line
# Use f-strings with alignment to make the columns line up
print()
print("=" * 30)
print(f"  Student: {name}")
print(...)   # score line
print(...)   # grade line
print(...)   # result line
print("=" * 30)
