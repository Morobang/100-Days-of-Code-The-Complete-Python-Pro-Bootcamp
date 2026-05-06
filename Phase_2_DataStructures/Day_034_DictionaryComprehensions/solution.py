# Day 34 Solutions

# Challenge 1
cubes = {n: n ** 3 for n in range(1, 11)}
print(cubes)

animals = ['cat', 'elephant', 'dog', 'ant']
word_lengths = {w: len(w) for w in animals}
print(word_lengths)

letter_positions = {ch: i for i, ch in enumerate('python')}
print(letter_positions)

# Challenge 2
inventory = {'apple': 50, 'banana': 0, 'cherry': 20, 'mango': 0, 'kiwi': 15}
in_stock = {k: v for k, v in inventory.items() if v > 0}
out_of_stock = {k: v for k, v in inventory.items() if v == 0}
doubled = {k: v * 2 for k, v in inventory.items() if v > 0}
print(in_stock)
print(out_of_stock)
print(doubled)

# Challenge 3
student_ids = {'Alice': 1001, 'Bob': 1002, 'Charlie': 1003, 'Diana': 1004}
id_to_name = {v: k for k, v in student_ids.items()}
print(id_to_name)
print(id_to_name.get(1003))

grades = dict.fromkeys(student_ids, 'unknown')
grades.update({'Alice': 'A', 'Bob': 'F', 'Charlie': 'B', 'Diana': 'A'})
print(grades)

# Challenge 4
sentence = input('Enter a sentence: ').lower()
words = sentence.split()
freq = {w: words.count(w) for w in set(words)}
repeated = {w: c for w, c in freq.items() if c > 1}
print('All words:', freq)
print('Repeated only:', repeated)

# Challenge 5
results = [
    ('Alice', 88), ('Bob', 45), ('Charlie', 72),
    ('Diana', 91), ('Eve', 55), ('Frank', 78)
]

scores_dict = {name: score for name, score in results}

grade_dict = {}
for name, score in results:
    if score >= 80:   grade_dict[name] = 'A'
    elif score >= 70: grade_dict[name] = 'B'
    elif score >= 60: grade_dict[name] = 'C'
    elif score >= 50: grade_dict[name] = 'D'
    else:             grade_dict[name] = 'F'

grade_set = {g for g in grade_dict.values()}
outcome_list = [f'{name} passed' if score >= 70 else f'{name} failed'
                for name, score in results]

print(scores_dict)
print(grade_dict)
print(grade_set)
print(outcome_list)
