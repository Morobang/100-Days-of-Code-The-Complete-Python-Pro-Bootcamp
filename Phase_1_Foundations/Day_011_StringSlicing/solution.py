# Day 11 — Solutions

# Challenge 1: First 3 and last 3 characters
word = input("Enter a word (at least 6 letters): ")
print("First 3:", word[:3])
print("Last 3: ", word[-3:])

# Challenge 2: Reverse a string with slicing
text = input("Enter text to reverse: ")
print(text[::-1])

# Challenge 3: Every other character
word = input("Enter a word: ")
print(word[::2])

# Challenge 4: Extract base name and extension from a filename
filename = input("Enter a filename (e.g. report_2024.txt): ")
dot_index = filename.find(".")
base = filename[:dot_index]
ext = filename[dot_index:]
print("Name:     ", base)
print("Extension:", ext)

# Challenge 5: First half and second half of a sentence
sentence = input("Enter a sentence: ")
midpoint = len(sentence) // 2
print("First half: ", sentence[:midpoint])
print("Second half:", sentence[midpoint:])
