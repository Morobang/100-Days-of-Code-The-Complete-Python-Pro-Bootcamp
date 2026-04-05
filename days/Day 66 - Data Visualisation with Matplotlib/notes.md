# Day 66 — Matplotlib

## Key syntax
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,6))
ax.plot(x, y, label='label', color='blue', linewidth=2)
ax.bar(x, y, color='green', alpha=0.7)
ax.scatter(x, y, c='red', s=50, alpha=0.6)
ax.hist(data, bins=20, edgecolor='black')
ax.pie(values, labels=labels, autopct='%1.1f%%')

ax.set_title('Title', fontsize=14)
ax.set_xlabel('X'); ax.set_ylabel('Y')
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xlim(0,10); ax.set_ylim(0,100)

plt.tight_layout()
plt.savefig('chart.png', dpi=150, bbox_inches='tight')
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12,10))
axes[0,0].plot(...)
```

## Interview tips
- Always use `fig, ax = plt.subplots()` not `plt.plot()` directly
- `tight_layout()` fixes overlapping labels
- For data engineering: use matplotlib for quick checks, plotly for dashboards
