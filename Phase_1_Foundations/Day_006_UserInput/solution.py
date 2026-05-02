# Day 6 — Solutions

# Challenge 1: Greeting
name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

# Challenge 2: Age from birth year
birth_year = int(input("What year were you born? "))
age = 2025 - birth_year
print("You are", age, "years old.")

# Challenge 3: Room area
length = float(input("Enter room length (metres): "))
width = float(input("Enter room width (metres): "))
area = length * width
print("Room area:", area, "square metres")

# Challenge 4: Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "°C is", fahrenheit, "°F")

# Challenge 5: Bill splitter
bill = float(input("Total bill amount: "))
people = int(input("Number of people: "))
tip_percent = float(input("Tip percentage (e.g. 15): "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print("-" * 30)
print("Bill:      R" + str(round(bill, 2)))
print("Tip:       R" + str(round(tip_amount, 2)))
print("Total:     R" + str(round(total, 2)))
print("Per person: R" + str(round(per_person, 2)))
