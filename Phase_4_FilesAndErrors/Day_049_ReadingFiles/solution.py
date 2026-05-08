# Day 49 Solutions
# Run from the Day_049_ReadingFiles folder so 'sample.txt' resolves correctly.

# Challenge 1
with open('sample.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
print(contents)

# Challenge 2
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Number of lines: {len(lines)}')

print()

# Challenge 3
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

print()

# Challenge 4
target = 'the'
count = 0
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        words = line.lower().split()
        count += words.count(target)
print(f"'{target}' appears {count} time(s)")

print()

# Challenge 5
longest = ''
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stripped = line.strip()
        if len(stripped) > len(longest):
            longest = stripped
print(f'Longest line ({len(longest)} chars):')
print(longest)
