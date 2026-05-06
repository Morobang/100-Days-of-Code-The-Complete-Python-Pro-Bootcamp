# Day 35 Solution: Word Counter

import string

print('Enter text (blank line to finish):')

lines = []
while True:
    line = input('> ')
    if line == '':
        break
    lines.append(line)

if not lines:
    print('No text entered.')
else:
    full_text = ' '.join(lines).lower()

    # Clean: strip punctuation from each token, drop empties
    raw_words = full_text.split()
    words = [w.strip(string.punctuation) for w in raw_words]
    words = [w for w in words if w]

    # Frequency dict
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    total = len(words)
    unique = len(freq)

    # Sort by frequency descending, then alphabetically for ties.
    # Build (-count, word) tuples so a plain .sort() gives the right order.
    sortable = [(-count, word) for word, count in freq.items()]
    sortable.sort()
    ranked = [(word, -neg_count) for neg_count, word in sortable]

    # Top 5
    top5 = ranked[:5]

    # Bottom 3 (least frequent, from the end of ranked)
    bottom3 = ranked[-3:]

    # Words appearing exactly once
    hapax = sorted([w for w, c in freq.items() if c == 1])

    # Unique first letters
    first_letters = sorted({w[0] for w in freq})

    # Report
    print(f'\nTotal words:  {total}')
    print(f'Unique words: {unique}')

    print('\nTop 5 most frequent:')
    for word, count in top5:
        print(f'  {word}: {count}')

    print('\n3 least frequent:')
    for word, count in bottom3:
        print(f'  {word}: {count}')

    print(f'\nWords appearing once ({len(hapax)}):')
    print(' ', ', '.join(hapax) if hapax else 'none')

    print(f'\nFirst letters used: {first_letters}')

    # Word lookup
    query = input('\nLook up a word: ').strip().lower().strip(string.punctuation)
    count = freq.get(query, 0)
    if count:
        print(f'"{query}" appears {count} time(s).')
    else:
        print(f'"{query}" was not found in the text.')
