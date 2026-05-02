# Day 5 — Solutions

# Challenge 1: Boolean variables with labels
is_student = True
is_employed = False
has_id = True
is_adult = True
print("Student:", is_student)
print("Employed:", is_employed)
print("Has ID:", has_id)
print("Adult:", is_adult)

# Challenge 2: bool() conversions
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool(-5))

# Challenge 3: None variable
middle_name = None
print(middle_name)
print(type(middle_name))

middle_name = "James"
print(middle_name)
print(type(middle_name))

# Challenge 4: Predictions and verification
# bool(0)       -> False  (0 is falsy)
# bool(100)     -> True   (non-zero is truthy)
# bool("")      -> False  (empty string is falsy)
# bool("False") -> True   (non-empty string is truthy — the content doesn't matter!)
# bool(None)    -> False  (None is falsy)
print(bool(0))
print(bool(100))
print(bool(""))
print(bool("False"))
print(bool(None))

# Challenge 5: User profile
username = "alex_dev"
age = 25
is_verified = True
bio = None

print(username, type(username))
print(age, type(age))
print(is_verified, type(is_verified))
print(bio, type(bio))
