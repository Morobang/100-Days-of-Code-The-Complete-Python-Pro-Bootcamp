# Day 33 Solutions

# Challenge 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(squares)
print(evens)
print(even_squares)

# Challenge 2
words = ['Python', 'is', 'a', 'great', 'programming', 'language']
upper = [w.upper() for w in words]
long = [w for w in words if len(w) > 3]
long_lengths = [len(w) for w in words if len(w) > 3]
print(upper)
print(long)
print(long_lengths)

# Challenge 3
scores = [('Alice', 88), ('Bob', 45), ('Charlie', 72), ('Diana', 91), ('Eve', 55)]
names = [name for name, score in scores]
score_vals = [score for name, score in scores]
passing = [name for name, score in scores if score >= 70]
labels = [f'{name}: {score}' for name, score in scores]
print(names)
print(score_vals)
print(passing)
print(labels)

# Challenge 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
doubled = [[val * 2 for val in row] for row in matrix]
big = [val for row in matrix for val in row if val > 4]
print(flat)
print(doubled)
print(big)

# Challenge 5
sentence = input('Enter a sentence: ')
all_words = sentence.lower().split()

unique_sorted = sorted(set(all_words))
long_titled = [w.title() for w in all_words if len(w) > 4]
by_length = sorted([(w, len(w)) for w in all_words], key=len, reverse=True)
alpha_only = [w for w in all_words if w.isalpha()]

print('Unique sorted:', unique_sorted)
print('Long words titled:', long_titled)
print('By length desc:', by_length)
print('Alpha only:', alpha_only)
