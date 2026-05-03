# Day 26 Project: Shopping List Manager
# Complete the TODOs below. Do not look at solution/ until you've tried.

shopping_list = []

print('=== Shopping List ===')

while True:
    # TODO: Print the menu (4 options: Add, Remove, View, Quit)

    choice = input('Choice: ').strip()

    if choice == '1':
        # TODO: Ask for an item name
        # TODO: Reject blank input (print a message and continue)
        # TODO: Append the item to shopping_list
        # TODO: Confirm with a message like "'Milk' added."
        pass

    elif choice == '2':
        # TODO: Ask for an item name to remove
        # TODO: If the item is in the list, remove it and confirm
        # TODO: If it's not in the list, print a 'not found' message
        pass

    elif choice == '3':
        # TODO: If the list is empty, print "Your list is empty."
        # TODO: Otherwise print each item numbered (1. Milk, 2. Eggs, ...)
        pass

    elif choice == '4':
        # TODO: Print "Goodbye!" and break out of the loop
        pass

    else:
        # TODO: Handle invalid menu choices
        pass
