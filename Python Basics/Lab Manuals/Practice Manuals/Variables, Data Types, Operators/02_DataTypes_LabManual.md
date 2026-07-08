# Lab Manual — Data Types in Python
### Module 1 | Python Programming Fundamentals
### Topic 2 of 3: Data Types

---

## Background

Every value in Python has a **data type** — it tells Python what kind of data you're working with and what operations are allowed on it.

### Core Built-in Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42`, `-7` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `str` | `"hello"` | Text / characters |
| `bool` | `True`, `False` | Logical values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `dict` | `{"key": "value"}` | Key-value pairs |
| `NoneType` | `None` | Absence of a value |

### Checking Types
Use the built-in `type()` function:
```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
```

### Type Conversion (Casting)
You can convert between types:
```python
int("5")     # → 5
float(3)     # → 3.0
str(100)     # → "100"
bool(0)      # → False
bool(1)      # → True
```

---

## Solved Tasks

---

### Task 1 — Identifying Types

**Objective:** Use `type()` to inspect several values.

```python
values = [42, 3.14, "Python", True, None, [1, 2], (3, 4), {"a": 1}]

for v in values:
    print(f"Value: {v!r:20} | Type: {type(v).__name__}")
```

**Output:**
```
Value: 42                   | Type: int
Value: 3.14                 | Type: float
Value: 'Python'             | Type: str
Value: True                 | Type: bool
Value: None                 | Type: NoneType
Value: [1, 2]               | Type: list
Value: (3, 4)               | Type: tuple
Value: {'a': 1}             | Type: dict
```

---

### Task 2 — Type Conversion

**Objective:** Convert values between types and handle a failed conversion.

```python
# int → float → str
num = 7
print(type(num), num)

num_float = float(num)
print(type(num_float), num_float)

num_str = str(num_float)
print(type(num_str), num_str)

# String to int
age_input = "22"
age = int(age_input)
print("Next year:", age + 1)
```

**Output:**
```
<class 'int'> 7
<class 'float'> 7.0
<class 'str'> 7.0
Next year: 23
```

---

### Task 3 — Strings and Their Properties

**Objective:** Explore common string operations.

```python
name = "Artificial Intelligence"

print(len(name))           # Length
print(name.upper())        # Uppercase
print(name.lower())        # Lowercase
print(name.replace("Intelligence", "Neural Networks"))
print(name[0:10])          # Slicing
print("AI" in name)        # Membership test
```

**Output:**
```
23
ARTIFICIAL INTELLIGENCE
artificial intelligence
Artificial Neural Networks
Artificial
False
```

---

### Task 4 — Booleans and Truthiness

**Objective:** Understand which values Python considers True or False.

```python
test_values = [0, 1, -5, "", "hello", [], [1, 2], None]

for val in test_values:
    print(f"bool({val!r}) = {bool(val)}")
```

**Output:**
```
bool(0) = False
bool(1) = True
bool(-5) = True
bool('') = False
bool('hello') = True
bool([]) = False
bool([1, 2]) = True
bool(None) = False
```

---

### Task 5 — Working with `None`

**Objective:** Use `None` as a placeholder and check for it correctly.

```python
result = None

if result is None:
    print("No result yet — computation pending.")
else:
    print("Result:", result)

# Assign and check again
result = 42
if result is None:
    print("Still nothing.")
else:
    print("Got a result:", result)
```

**Output:**
```
No result yet — computation pending.
Got a result: 42
```

---

## Student Practice Tasks

Solve the following tasks on your own. No solutions are provided here — attempt each one independently.

1. Create one variable of each core type (`int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `NoneType`) and print both the value and its type using `type()`.

2. Ask the user to enter their age as input (which is always a string). Convert it to an integer, add 5, and print the result.

3. Create a string with your full name. Print its length, convert it to uppercase, replace your first name with `"Student"`, and check whether the letter `"a"` appears in it.

4. Write a program that demonstrates the difference between `int` and `float` division: divide `7` by `2` using `/` and `//` and print both results with their types.

5. Given the string `"100"`, convert it to an integer and a float. Print all three versions (original string, int, float) along with their types.

6. Create a list of 5 numbers. Print the list, its type, its length, and the type of the first element.

7. Create a dictionary storing a student's `name`, `age`, `grade`, and `is_enrolled` (bool). Print each key-value pair along with the type of the value.

8. Write a program that tests truthiness: for each of the following — `0`, `0.0`, `""`, `"0"`, `[]`, `{}`, `None`, `False` — print whether Python treats it as truthy or falsy.

9. Convert the float `9.99` to an integer and explain in a comment what happens to the decimal part. Then convert it to a string and demonstrate that you can no longer do arithmetic on it.

10. Write a program that uses `isinstance()` to check whether a given variable is of type `int`, `float`, or `str`, and prints a different message for each case.
