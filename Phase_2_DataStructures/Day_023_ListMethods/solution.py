# Day 23 Solutions

# Challenge 1
list1 = ['milk', 'eggs', 'bread']
list2 = ['butter', 'cheese', 'yogurt']

list1.extend(list2)
print('extend result:', list1)  # 6 flat items

list3 = ['milk', 'eggs', 'bread']
list3.append(list2)
print('append result:', list3)  # list2 added as a nested list

# Challenge 2
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
items.remove('banana')
removed = items.pop()
print('Removed:', removed)
del items[1]
print(items)

# Challenge 3
names = ['Charlie', 'alice', 'Bob', 'diana', 'Eve']

alpha = sorted(names, key=str.lower)
print('Alphabetical:', alpha)
print('Original unchanged:', names)

by_len = sorted(names, key=len)
print('By length (short first):', by_len)

by_len_desc = sorted(names, key=len, reverse=True)
print('By length (long first):', by_len_desc)

# Challenge 4
history = []
while True:
    action = input('Action: ').strip()
    if action == 'quit':
        break
    elif action == 'back':
        if len(history) > 1:
            history.pop()
            print('Current page:', history[-1])
        elif len(history) == 1:
            history.pop()
            print('No more history.')
        else:
            print('No history.')
    else:
        history.append(action)
        print('Current page:', history[-1])

# Challenge 5
tasks = []
while True:
    name = input('Task name (or "done"): ')
    if name == 'done':
        break
    priority = int(input('Priority (1=high, 3=low): '))
    tasks.append((priority, name))

tasks.sort()  # tuples sort by first element naturally

print('\nTask list:')
for i, (priority, task) in enumerate(tasks, 1):
    print(f'Task {i}: [{priority}] {task}')
