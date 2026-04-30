# Setup Guide

Everything you need to get started with this course.

---

## 1. Install Python

### Windows
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the latest Python 3.x installer
3. Run the installer — **check the box "Add Python to PATH"** before clicking Install
4. Verify: open Command Prompt and run `python --version`

### Mac
1. Go to [python.org/downloads](https://python.org/downloads) and download the macOS installer, or
2. If you have Homebrew: `brew install python3`
3. Verify: open Terminal and run `python3 --version`

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

---

## 2. Install Jupyter

Jupyter lets you run the `.ipynb` notebook files in this course.

```bash
pip install notebook
```

To launch Jupyter:
```bash
jupyter notebook
```

This opens a browser window. Navigate to the day folder you want and open the `.ipynb` file.

---

## 3. VS Code (alternative to Jupyter)

VS Code can open and run `.ipynb` files directly without launching Jupyter in a browser.

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com)
2. Open VS Code → Extensions (Ctrl+Shift+X) → search for "Jupyter" → Install
3. Open any `.ipynb` file and VS Code will handle it

This is the recommended option if you're comfortable with editors.

---

## 4. Fork and clone the repo

1. Click "Fork" at the top right of the GitHub repo page
2. On your forked repo, click "Code" → copy the URL
3. In your terminal:

```bash
git clone https://github.com/YOUR_USERNAME/python-100-days
cd python-100-days
```

---

## 5. Verify your setup

Run these in a terminal to confirm everything works:

```bash
python --version        # should show Python 3.x.x
pip --version           # should show pip version
jupyter --version       # should show jupyter version
```

Then open `Phase_1_Foundations/Day_001_PrintingAndOutput/01_learn.ipynb` and run the first cell. If it prints `Hello, World!` you're good to go.

---

## Troubleshooting

**"python is not recognized" (Windows)**
- Re-run the Python installer and check "Add Python to PATH"
- Or search for "Environment Variables" in Windows settings and add Python manually

**"pip is not recognized"**
- Try `python -m pip install notebook` instead of `pip install notebook`

**Kernel not found in Jupyter**
- Run `pip install ipykernel` then `python -m ipykernel install --user`
- Restart Jupyter

**Wrong Python version (Mac)**
- Mac comes with Python 2. Make sure you're running `python3` not `python`
- When installing packages use `pip3` not `pip`
