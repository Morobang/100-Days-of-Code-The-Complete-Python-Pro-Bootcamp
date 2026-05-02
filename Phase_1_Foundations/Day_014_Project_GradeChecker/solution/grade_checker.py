# Grade Checker — Day 14 Solution

name = input("Enter student name: ").strip().title()
score = int(input("Enter score (0-100): "))

while score < 0 or score > 100:
    print("Score must be between 0 and 100. Try again.")
    score = int(input("Enter score (0-100): "))

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

print()
print("=" * 30)
print(f"  Student: {name}")
print(f"  Score:   {score}/100")
print(f"  Grade:   {grade}")
print(f"  Result:  {result}")
print("=" * 30)
