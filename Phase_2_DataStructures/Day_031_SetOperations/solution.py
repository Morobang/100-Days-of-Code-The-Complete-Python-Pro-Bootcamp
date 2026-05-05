# Day 31 Solutions

# Challenge 1
cart = {'apple', 'banana', 'cherry'}
cart |= {'mango', 'kiwi', 'banana'}
print('After |=:', cart)
cart -= {'banana', 'kiwi'}
print('After -=:', cart)  # {'apple', 'cherry', 'mango'}

# Challenge 2
mon = {'Alice', 'Bob', 'Charlie', 'Diana'}
tue = {'Bob', 'Charlie', 'Eve'}
wed = {'Alice', 'Charlie', 'Frank'}
thu = {'Charlie', 'Diana', 'Eve', 'Frank'}

print('All four days:', mon & tue & wed & thu)
print('At least one day:', sorted(mon | tue | wed | thu))
print('Mon but not Thu:', mon - thu)

# Exactly two days — count membership with a loop
all_students = mon | tue | wed | thu
exactly_two = set()
for name in all_students:
    count = 0
    if name in mon: count += 1
    if name in tue: count += 1
    if name in wed: count += 1
    if name in thu: count += 1
    if count == 2:
        exactly_two.add(name)
print('Exactly two days:', sorted(exactly_two))

# Challenge 3
maths   = {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
science = {'Bob', 'Charlie', 'Frank', 'Grace'}
english = {'Alice', 'Charlie', 'Diana', 'Grace', 'Heidi'}

print('All three:', maths & science & english)
print('Maths & Science, not English:', (maths & science) - english)

all_s = maths | science | english
one_course = set()
for name in all_s:
    count = 0
    if name in maths:   count += 1
    if name in science: count += 1
    if name in english: count += 1
    if count == 1:
        one_course.add(name)
print('Only one course:', sorted(one_course))
print('Total unique students:', len(all_s))

# Challenge 4
blocklist = {'spam', 'ads', 'promo', 'click', 'buy', 'free', 'win'}
sentence = input('Enter a sentence: ').lower()
words = set(sentence.split())

clean = words - blocklist
flagged = words & blocklist
print('Clean words:', sorted(clean))
print('Flagged words:', sorted(flagged))
print('Is clean:', words.isdisjoint(blocklist))

words &= clean
print('Filtered sentence:', ' '.join(sorted(words)))

# Challenge 5
friends = {
    'Alice':   {'Bob', 'Charlie', 'Diana'},
    'Bob':     {'Alice', 'Charlie', 'Eve'},
    'Charlie': {'Alice', 'Bob', 'Diana', 'Frank'},
    'Diana':   {'Alice', 'Charlie'},
    'Eve':     {'Bob', 'Frank'},
    'Frank':   {'Charlie', 'Eve'}
}

user = input('Enter your name: ').strip()
if user not in friends:
    print('User not found.')
else:
    my_friends = friends[user]
    print('Direct friends:', sorted(my_friends))

    candidates = set()
    for friend in my_friends:
        candidates |= friends[friend]
    recommendations = candidates - my_friends - {user}

    print('\nRecommendations:')
    for person in sorted(recommendations):
        mutuals = my_friends & friends[person]
        print(f'  {person} — {len(mutuals)} mutual friend(s): {sorted(mutuals)}')
