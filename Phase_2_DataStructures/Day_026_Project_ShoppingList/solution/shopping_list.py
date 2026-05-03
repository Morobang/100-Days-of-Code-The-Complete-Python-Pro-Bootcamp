# Day 26 Solution: Shopping List Manager

shopping_list = []

print('=== Shopping List ===')

while True:
    print('\n1. Add item')
    print('2. Remove item')
    print('3. View list')
    print('4. Quit')

    choice = input('Choice: ').strip()

    if choice == '1':
        item = input('Item to add: ').strip()
        if item == '':
            print('Item name cannot be blank.')
        else:
            shopping_list.append(item)
            print(f"'{item}' added.")

    elif choice == '2':
        item = input('Item to remove: ').strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' is not in your list.")

    elif choice == '3':
        if len(shopping_list) == 0:
            print('Your list is empty.')
        else:
            for i, item in enumerate(shopping_list, 1):
                print(f'{i}. {item}')

    elif choice == '4':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Please enter 1, 2, 3, or 4.')
