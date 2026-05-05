# Day 32 Solution: Contact Book

contacts = {}

print('=== Contact Book ===')

while True:
    print('\n1. Add contact')
    print('2. View all')
    print('3. Search')
    print('4. Update')
    print('5. Delete')
    print('6. Quit')

    choice = input('Choice: ').strip()

    if choice == '1':
        name = input('Name: ').strip()
        if name == '':
            print('Name cannot be blank.')
            continue
        # Case-insensitive duplicate check
        for existing in contacts:
            if existing.lower() == name.lower():
                print(f"'{existing}' already exists.")
                break
        else:
            phone = input('Phone: ').strip()
            email = input('Email: ').strip()
            contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added.")

    elif choice == '2':
        if not contacts:
            print('No contacts yet.')
        else:
            for name in sorted(contacts):
                info = contacts[name]
                print(f"{name:15} | {info['phone']:15} | {info['email']}")

    elif choice == '3':
        query = input('Search: ').strip().lower()
        found = None
        for name in contacts:
            if name.lower() == query:
                found = name
                break
        if found:
            info = contacts[found]
            print(f"{found}: {info['phone']} | {info['email']}")
        else:
            print('Not found.')

    elif choice == '4':
        query = input('Contact to update: ').strip().lower()
        found = None
        for name in contacts:
            if name.lower() == query:
                found = name
                break
        if not found:
            print('Not found.')
        else:
            field = input('Update (phone/email): ').strip().lower()
            if field in ('phone', 'email'):
                new_val = input(f'New {field}: ').strip()
                contacts[found][field] = new_val
                print(f"'{found}' {field} updated.")
            else:
                print("Enter 'phone' or 'email'.")

    elif choice == '5':
        query = input('Delete: ').strip().lower()
        found = None
        for name in contacts:
            if name.lower() == query:
                found = name
                break
        if found:
            contacts.pop(found)
            print(f"'{found}' deleted.")
        else:
            print('Not found.')

    elif choice == '6':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Enter 1–6.')
