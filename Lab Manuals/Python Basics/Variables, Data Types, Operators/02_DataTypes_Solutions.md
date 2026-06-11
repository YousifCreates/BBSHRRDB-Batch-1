# Solutions — Data Types in Python
### Module 1 | Python Programming Fundamentals
### Topic 2 of 3: Data Types

---

> **Note for Instructors:** Solutions to the 10 student practice tasks from the Data Types Lab Manual.

---

### Solution 1 — One of Each Type

```python
i = 10
f = 3.14
s = "hello"
b = True
l = [1, 2, 3]
t = (4, 5, 6)
d = {"key": "value"}
n = None

for val in [i, f, s, b, l, t, d, n]:
    print(f"Value: {val!r} | Type: {type(val).__name__}")
```

---

### Solution 2 — Age Input Conversion

```python
age_input = input("Enter your age: ")  # e.g. "20"
age = int(age_input)
print("In 5 years you will be:", age + 5)
```

---

### Solution 3 — String Operations on Name

```python
full_name = "Yousif Ahmed"
print("Length:", len(full_name))
print("Uppercase:", full_name.upper())
print("Replaced:", full_name.replace("Yousif", "Student"))
print("'a' in name:", "a" in full_name)
```

---

### Solution 4 — Int vs Float Division

```python
a = 7
b = 2

result_float = a / b
result_int   = a // b

print(f"{a} / {b}  = {result_float} ({type(result_float).__name__})")
print(f"{a} // {b} = {result_int}   ({type(result_int).__name__})")
```

---

### Solution 5 — String to Int and Float

```python
original = "100"
as_int   = int(original)
as_float = float(original)

print(f"Original: {original!r}  Type: {type(original).__name__}")
print(f"Int:      {as_int}      Type: {type(as_int).__name__}")
print(f"Float:    {as_float}    Type: {type(as_float).__name__}")
```

---

### Solution 6 — List Exploration

```python
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)
print("Type:", type(numbers))
print("Length:", len(numbers))
print("First element type:", type(numbers[0]))
```

---

### Solution 7 — Dictionary with Types

```python
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A",
    "is_enrolled": True
}

for key, value in student.items():
    print(f"{key}: {value!r} — Type: {type(value).__name__}")
```

---

### Solution 8 — Truthiness Test

```python
test_values = [0, 0.0, "", "0", [], {}, None, False]

for val in test_values:
    result = "Truthy" if bool(val) else "Falsy"
    print(f"bool({val!r}) → {result}")
```

---

### Solution 9 — Float to Int Conversion

```python
f = 9.99
i = int(f)   # Decimal part is TRUNCATED (not rounded) → 9
print(f"float: {f}  →  int: {i}")  # 9.99 → 9

s = str(f)
print(f"As string: {s!r}")
# Cannot do arithmetic:
# print(s + 1)  # This would raise a TypeError
```

---

### Solution 10 — isinstance() Check

```python
def check_type(val):
    if isinstance(val, int):
        print(f"{val!r} is an integer.")
    elif isinstance(val, float):
        print(f"{val!r} is a float.")
    elif isinstance(val, str):
        print(f"{val!r} is a string.")
    else:
        print(f"{val!r} is none of int, float, or str.")

check_type(42)
check_type(3.14)
check_type("hello")
check_type([1, 2])
```
