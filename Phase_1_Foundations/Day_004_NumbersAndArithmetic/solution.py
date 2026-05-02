import math

# Challenge 1: Area of rectangle
width = 12
height = 7
area = width * height
print("Area:", area)

# Challenge 2: Items you can buy and change
budget = 500
price = 37
items = budget // price
change = budget % price
print("Items:", items)
print("Change:", change)

# Challenge 3: Hypotenuse
a = 3
b = 4
hypotenuse_sqrt = math.sqrt(a**2 + b**2)
hypotenuse_pow = (a**2 + b**2) ** 0.5
print("Hypotenuse (sqrt):", hypotenuse_sqrt)
print("Hypotenuse (**):", hypotenuse_pow)

# Challenge 4: Pizza area
radius = 15
area = math.pi * radius ** 2
print("Pizza area:", math.floor(area))

# Challenge 5: Celsius to Fahrenheit
c1, c2, c3 = 0, 100, 37
f1 = (c1 * 9/5) + 32
f2 = (c2 * 9/5) + 32
f3 = (c3 * 9/5) + 32
print(f"{c1}°C = {f1}°F")
print(f"{c2}°C = {f2}°F")
print(f"{c3}°C = {f3}°F")
