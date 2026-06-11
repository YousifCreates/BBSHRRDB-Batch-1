# 📋 Week 1 — Revision Sheet

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ⚡ Key Syntax Quick Reference

```python
# Launch the REPL (in terminal)
python3

# Exit the REPL
exit()

# Run a script (in terminal)
python3 filename.py

# print() — basic usage
print("Hello")

# print() — multiple values (space between by default)
print("Name:", "Alice", "Age:", 30)

# print() — custom separator
print("A", "B", "C", sep="-")      # A-B-C
print("2024", "01", "15", sep="/") # 2024/01/15

# print() — custom end character
print("Loading...", end="")         # no newline
print("Done!")                      # continues on same line

# print() — blank line
print()

# Comment (Python ignores this)
# This is a single-line comment

# String repetition (preview of Week 2)
print("=" * 30)   # 30 equal signs

# Data types
"Hello"    # str   (string)
42         # int   (integer)
3.14       # float (decimal)
True       # bool  (boolean — capital T)
False      # bool  (boolean — capital F)
```

---

## 📖 Important Functions — Week 1

| Function | Syntax | What It Does |
|---|---|---|
| `print()` | `print(value, ..., sep=" ", end="\n")` | Displays output to the screen |
| `exit()` | `exit()` | Exits the Python REPL |

---

## 📝 Cheat Sheet

| Concept | Key Point |
|---|---|
| **REPL** | Interactive shell. Launch with `python3`. Exit with `exit()`. |
| **Script** | A `.py` file. Run with `python3 filename.py`. |
| **`print()`** | Displays output. Default separator is space. Default end is newline `\n`. |
| **Comments** | Start with `#`. Python completely ignores them. For human readers only. |
| **Strings** | Text must be in quotes: `"Hello"` or `'Hello'`. |
| **Integers** | Whole numbers, no quotes: `42`. |
| **Floats** | Decimal numbers, no quotes: `3.14`. |
| **Booleans** | Exactly `True` or `False`. Capital first letter. |
| **Interpreted** | Python runs code line by line at runtime — no compilation needed. |
| **`sep=`** | Controls what goes between values in `print()`. Default: `" "`. |
| **`end=`** | Controls what comes after all values. Default: `"\n"` (newline). |

---

## 🧠 MCQs (Multiple Choice Questions)

**Circle the correct answer.**

**1.** What does REPL stand for?

- A) Run-Execute-Print-Loop
- B) Read-Eval-Print-Loop ✅
- C) Read-Execute-Process-Loop
- D) Run-Edit-Print-Log

---

**2.** What is the output of `print("A", "B", "C", sep="-")`?

- A) `A B C`
- B) `A-B-C` ✅
- C) `ABC`
- D) `A, B, C`

---

**3.** Which of the following is a valid Python boolean?

- A) `true`
- B) `TRUE`
- C) `True` ✅
- D) `"True"`

---

**4.** What does `print()` with no arguments do?

- A) Causes an error
- B) Prints the word `None`
- C) Prints a blank line ✅
- D) Does nothing at all

---

**5.** How do you print a backslash `\` in Python?

- A) `print("\")`
- B) `print("\\")`  ✅
- C) `print("/")`
- D) `print(BACKSLASH)`

---

**6.** What is the default value of `end=` in `print()`?

- A) `" "` (a space)
- B) `","` (a comma)
- C) `"\n"` (a newline) ✅
- D) `""` (nothing)

---

**7.** Which command runs a Python script from the terminal?

- A) `run hello.py`
- B) `execute hello.py`
- C) `python3 hello.py` ✅
- D) `start hello.py`

---

**8.** What symbol is used to start a comment in Python?

- A) `//`
- B) `--`
- C) `/*`
- D) `#` ✅

---

## ✅ True / False

Mark T (True) or F (False):

| # | Statement | Answer |
|---|---|---|
| 1 | Python is a compiled language | **F** |
| 2 | The REPL runs code line by line interactively | **T** |
| 3 | Comments are displayed as output when the script runs | **F** |
| 4 | `print("Hello")` and `Print("Hello")` do the same thing | **F** |
| 5 | `print()` adds a newline after each output by default | **T** |
| 6 | `true` is a valid Python boolean | **F** |
| 7 | You can use both `"..."` and `'...'` for strings | **T** |
| 8 | `print("A", "B", sep="")` outputs `A B` | **F** (outputs `AB`) |
| 9 | `exit()` closes the REPL | **T** |
| 10 | `.py` is the standard extension for Python script files | **T** |

---

## 📝 Fill in the Blanks

Complete each statement:

1. The Python interactive shell is called the _______ (Read-Eval-Print Loop). **Answer: REPL**

2. To print without a newline at the end, use `print("text", end=_________)`. **Answer: `""`**

3. The symbol used for a Python comment is _______. **Answer: `#`**

4. Python's boolean values are _______ and _______. **Answer: `True`, `False`**

5. To run `hello.py` from the terminal, type: `_______ hello.py`. **Answer: `python3`**

6. `print("A", "B", sep="_")` outputs: _______. **Answer: `A_B`**

7. A Python script file has the extension _______. **Answer: `.py`**

8. To print a blank line in Python, use: `_______()`. **Answer: `print`**

---

## 💼 Interview Questions — Week 1 Topics

**Q1: What is the difference between an interpreted and compiled language?**
> Interpreted languages (like Python) execute code line by line at runtime using an interpreter. Compiled languages (like C) translate all code into machine code before execution. Interpreted languages are slower at runtime but faster to develop and debug. Python's interpreted nature makes it ideal for scripting and automation where development speed matters more than raw execution speed.

**Q2: What is the Python REPL and when would you use it?**
> The REPL (Read-Eval-Print Loop) is Python's interactive shell, launched by typing `python3`. It reads one line of code, evaluates it, prints the result, and loops back. I use the REPL for quick experiments, testing small snippets of code, or exploring how a function behaves without creating a full script.

**Q3: What are the four main data types in Python?**
> The four basic types are: `str` (strings — text in quotes), `int` (whole numbers), `float` (decimal numbers), and `bool` (True or False). These cover the vast majority of simple programming tasks.

**Q4: What does the `#` symbol do in Python?**
> `#` starts a comment. Python completely ignores everything after `#` on that line. Comments are for human readers — explaining what code does, why a decision was made, or leaving notes for future developers.

**Q5: How would you print `A/B/C` using `print()` with separate arguments?**
> `print("A", "B", "C", sep="/")` — the `sep` parameter controls what appears between each value.

---

## 🎯 Mini Quiz

Test yourself — close this sheet and answer from memory:

1. What command launches the Python REPL?
2. What does `print("=" * 10)` output?
3. What does `end=""` do in `print()`?
4. How do you write a Python comment?
5. What is `True` — what data type is it?
6. How is Python different from C or Java in terms of execution?
7. What is the file extension for Python scripts?
8. What does `print()` with no arguments output?

*(Answers are throughout this Revision Sheet — search if needed)*

---

## 🔗 Cross References

| | |
|---|---|
| **Previous Topic** | [Challenge Lab — ASCII Art](Challenge_Lab.md) |
| **Next Week** | Week 2 — Variables, Data Types & Operators |
| **Course README** | [Course Overview](../README.md) |
| **Week README** | [Week 1 Overview](README.md) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*← [Challenge Lab](Challenge_Lab.md) | Next Week: Week 2 — Basic Python Syntax →*
