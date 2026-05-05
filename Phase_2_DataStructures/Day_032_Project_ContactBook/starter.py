# Day 32 Project: Contact Book
# Complete the TODOs below. Do not look at solution/ until you've tried.

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
        # TODO: Ask for name, phone, and email
        # TODO: Reject if the name already exists (case-insensitive check)
        # TODO: Store as contacts[name] = {'phone': ..., 'email': ...}
        # TODO: Confirm with a message
        pass

    elif choice == '2':
        # TODO: If empty, print a message
        # TODO: Otherwise print each contact in alphabetical order
        #        Format: Name  | phone | email
        pass

    elif choice == '3':
        # TODO: Ask for a name to search
        # TODO: Search case-insensitively (compare lowercased keys)
        # TODO: Print the contact's details, or 'Not found'
        pass

    elif choice == '4':
        # TODO: Ask for the contact name to update
        # TODO: If not found, print a message
        # TODO: Ask which field to update: phone or email
        # TODO: Update and confirm
        pass

    elif choice == '5':
        # TODO: Ask for the contact name to delete
        # TODO: Remove it with .pop() — handle not found gracefully
        # TODO: Confirm deletion or print 'Not found'
        pass

    elif choice == '6':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Enter 1–6.')
