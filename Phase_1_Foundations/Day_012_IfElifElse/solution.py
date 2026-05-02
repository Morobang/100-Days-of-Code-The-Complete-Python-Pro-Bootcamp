# Day 12 — Solutions

# Challenge 1: Positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# Challenge 2: Age category
age = int(input("Enter your age: "))
if age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")

# Challenge 3: Password check
password = input("Enter password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# Challenge 4: Larger of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(f"The larger number is {a}")
elif b > a:
    print(f"The larger number is {b}")
else:
    print("They are equal")

# Challenge 5: Letter grade and pass/fail
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if score >= 60:
    result = "Pass"
else:
    result = "Fail"

print(f"Grade: {grade} — {result}")
