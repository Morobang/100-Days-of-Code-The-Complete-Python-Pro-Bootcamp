# Day 36 Solutions

# Challenge 1
def print_greeting():
    print('Hello, welcome!')
    print('Ready to code today.')

print_greeting()
print_greeting()
print_greeting()

# Challenge 2
def print_separator():
    print('-' * 40)

def print_title():
    print_separator()
    print('        MY PYTHON JOURNAL')
    print_separator()

print_title()

# Challenge 3
def show_menu():
    print('1. Add item')
    print('2. View items')
    print('3. Quit')

show_menu()
choice = input('Choice: ')
if choice == '1':
    print('You chose: Add item')
elif choice == '2':
    print('You chose: View items')
elif choice == '3':
    print('You chose: Quit')
else:
    print('Invalid choice.')

# Challenge 4
def print_name():
    print('Name: Alex Smith')

def print_role():
    print('Role: Python Student')

def print_skills():
    print('Skills: Python, Problem-solving, Curiosity')

def print_goal():
    print('Goal: Build real projects with Python by year end.')

def print_profile():
    print('=' * 35)
    print_name()
    print('-' * 35)
    print_role()
    print('-' * 35)
    print_skills()
    print('-' * 35)
    print_goal()
    print('=' * 35)

print_profile()

# Challenge 5
def print_report_header():
    print('*' * 40)
    print('        MORNING REPORT')
    print('*' * 40)

def print_date_section():
    date = input('Today\'s date: ')
    print(f'Date: {date}')

def print_mood_section():
    mood = input('Mood (1=low, 5=great): ')
    messages = {'1': 'Tough day — keep going.', '2': 'A bit low — you\'ve got this.',
                '3': 'Okay — make it count.', '4': 'Good energy today!',
                '5': 'Excellent — have a great day!'}
    print(messages.get(mood, 'Stay positive!'))

def print_tasks_section():
    print('Today\'s tasks:')
    for i in range(1, 4):
        task = input(f'  Task {i}: ')
        print(f'  {i}. {task}')

def print_goal_section():
    print('Reminder: Small steps every day build big skills.')

def print_report_footer():
    print('*' * 40)
    print('         Have a great day!')
    print('*' * 40)

def run_report():
    print_report_header()
    print_date_section()
    print_mood_section()
    print_tasks_section()
    print_goal_section()
    print_report_footer()

run_report()
