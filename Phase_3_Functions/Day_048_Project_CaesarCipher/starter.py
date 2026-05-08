# Day 48 Project: Caesar Cipher
# Complete the TODOs. Do not look at solution/ until you've tried.

# TODO: Write encode(text, shift)
#       Loop over each character in text.
#       If it is a letter (ch.isalpha()):
#         - Find the base: ord('A') if uppercase, ord('a') if lowercase.
#         - Shift: chr((ord(ch) - base + shift) % 26 + base)
#       Otherwise leave the character unchanged.
#       Return the full encoded string.

# TODO: Write decode(text, shift)
#       Hint: decoding is encoding with the shift negated.

# TODO: Write the main loop — show the menu, handle each choice:
#       1 → input text, input shift (int), print encode(text, shift)
#       2 → input text, input shift (int), print decode(text, shift)
#       3 → quit

print('=== Caesar Cipher ===')
