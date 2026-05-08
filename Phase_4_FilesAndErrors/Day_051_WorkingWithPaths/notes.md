# Working with Paths — Quick Reference

## Import
```python
import os
import os.path
```

## Current Working Directory
```python
os.getcwd()           # full path to where Python is running
```

## Building Paths (Cross-platform)
```python
os.path.join('folder', 'sub', 'file.txt')
# Windows: 'folder\\sub\\file.txt'
# Mac/Linux: 'folder/sub/file.txt'
```
Never hard-code `\\` or `/` — use `os.path.join()`.

## Checking Existence
```python
os.path.exists('file.txt')    # True if path exists (file or dir)
os.path.isfile('file.txt')    # True only if it's a file
os.path.isdir('folder')       # True only if it's a directory
```

## Path Components
```python
path = '/home/user/docs/report.txt'
os.path.basename(path)    # 'report.txt'
os.path.dirname(path)     # '/home/user/docs'
os.path.splitext(path)    # ('/home/user/docs/report', '.txt')
```

## Listing Directory Contents
```python
os.listdir('.')           # list of names in current directory
os.listdir('/some/path')  # list of names in that directory
```

## Modern Alternative: pathlib
```python
from pathlib import Path

p = Path('folder') / 'sub' / 'file.txt'  # / operator joins paths
p.exists()
p.is_file()
p.suffix      # '.txt'
p.stem        # 'file'
p.parent      # Path('folder/sub')
list(Path('.').iterdir())  # like os.listdir
```
