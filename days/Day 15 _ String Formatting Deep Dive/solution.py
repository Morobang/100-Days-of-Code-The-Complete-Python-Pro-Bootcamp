# Day 15 — String Formatting — SOLUTIONS

# Exercise 1 — receipt
items = [('Tekken 8', 999), ('PS5 Controller', 1299)]
width = 25
print(f"{'Item':<{width-8}} {'Price':>8}")
print('-' * width)
total = 0
for name, price in items:
    print(f'{name:<{width-8}} R{price:>7.2f}')
    total += price
print('-' * width)
print(f"{'TOTAL':<{width-8}} R{total:>7.2f}")


# Exercise 2 — progress bar
def progress_bar(current, total, width=20):
    filled = int(width * current / total) if total else 0
    bar = '█' * filled + '░' * (width - filled)
    pct = int(100 * current / total) if total else 0
    print(f'[{bar}] {pct}%')


# Exercise 3 — table
def print_table(headers, rows):
    col_widths = [max(len(str(headers[i])), max(len(str(r[i])) for r in rows))
                  for i in range(len(headers))]
    def fmt_row(row):
        return '  '.join(str(v).ljust(col_widths[i]) for i, v in enumerate(row))
    print(fmt_row(headers))
    print('-' * sum(col_widths + [2 * (len(headers)-1)]))
    for row in rows:
        print(fmt_row(row))
