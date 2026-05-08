# Day 48 Solution: Caesar Cipher

def encode(text, shift):
    result = ''
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def decode(text, shift):
    return encode(text, -shift)

print('=== Caesar Cipher ===')

while True:
    print('\n1. Encode')
    print('2. Decode')
    print('3. Quit')

    choice = input('Choice: ').strip()

    if choice == '1':
        text = input('Text: ')
        shift = int(input('Shift: '))
        print('Encoded:', encode(text, shift))

    elif choice == '2':
        text = input('Text: ')
        shift = int(input('Shift: '))
        print('Decoded:', decode(text, shift))

    elif choice == '3':
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Enter 1–3.')
