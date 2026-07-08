# Lab Manual — Variables in Python
### Module 1 | Python Programming Fundamentals
### Topic 1 of 3: Variables

---

## Background

A **variable** is a named container that stores a value in memory. In Python, you don't need to declare a variable's type before using it — Python figures it out automatically when you assign a value.

**Key rules for variable names:**
- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Can contain letters, digits, and underscores
- Case-sensitive (`name` and `Name` are different variables)
- Cannot use Python reserved keywords (like `if`, `for`, `while`)

**Assignment** is done using the `=` operator:
```python
age = 25
name = "Ali"
is_student = True
```

Python also supports **multiple assignment** in one line:
```python
x, y, z = 1, 2, 3
a = b = c = 0
```

---

## Solved Tasks

---

### Task 1 — Declare and Print Variables

**Objective:** Create variables of different kinds and print them.

```python
# Declare variables
student_name = "Ahmed"
student_age = 20
student_gpa = 3.8

# Print them
print("Name:", student_name)
print("Age:", student_age)
print("GPA:", student_gpa)
```

**Output:**
```
Name: Ahmed
Age: 20
GPA: 3.8
```

---

### Task 2 — Multiple Assignment

**Objective:** Assign multiple variables in a single line and swap two values.

```python
# Multiple assignment
x, y = 10, 20
print("Before swap — x:", x, "y:", y)

# Swap without a temp variable
x, y = y, x
print("After swap  — x:", x, "y:", y)
```

**Output:**
```
Before swap — x: 10 y: 20
After swap  — x: 20 y: 10
```

---

### Task 3 — Reassigning Variables

**Objective:** Understand that a variable can change its value (and even its type) during a program.

```python
score = 100
print("Initial score:", score)

score = score + 50
print("After bonus:", score)

score = "Disqualified"
print("Final status:", score)
```

**Output:**
```
Initial score: 100
After bonus: 150
Final status: Disqualified
```

---

### Task 4 — Using `id()` to Understand Memory

**Objective:** Show that reassigning a variable points it to a new memory location.

```python
x = 5
print("Value:", x, "| Memory ID:", id(x))

x = 10
print("Value:", x, "| Memory ID:", id(x))
```

**Output (IDs will differ on your machine):**
```
Value: 5  | Memory ID: 140720012345678
Value: 10 | Memory ID: 140720012345900
```
> The `id()` function returns the memory address of the object the variable points to. Reassigning changes the address.

---

### Task 5 — Constants Convention

**Objective:** Understand Python's convention for constants (Python has no true `const` keyword).

```python
# By convention, constants are written in ALL_CAPS
MAX_STUDENTS = 30
PI = 3.14159
UNIVERSITY_NAME = "FAST NUCES"

print(f"University: {UNIVERSITY_NAME}")
print(f"Max students per class: {MAX_STUDENTS}")
print(f"Value of PI: {PI}")
```

**Output:**
```
University: FAST NUCES
Max students per class: 30
Value of PI: 3.14159
```

---

## Student Practice Tasks

Solve the following tasks on your own. No solutions are provided here — attempt each one independently.

1. Create three variables: your full name, your age, and your city. Print all three on separate lines.

2. Assign the value `50` to a variable `a` and `80` to a variable `b`. Swap their values and print both variables after the swap.

3. Create a variable `counter` starting at `0`. Add `1` to it five times using reassignment (one line per increment), then print the final value.

4. Create two variables with the same value (`x = 5`, `y = 5`). Use `id()` to check whether they point to the same memory address. Print the result and explain what you observe.

5. Declare a variable `temperature` and assign it `36.6`. Then reassign it to the string `"Fever"`. Print both values and check that Python allowed the type change.

6. Write a program that stores the name, roll number, and CGPA of a student in three separate variables and prints them in a formatted sentence. Example output: `Student Ali (Roll: 101) has a CGPA of 3.75.`

7. Create five variables in a single line using multiple assignment (e.g., days of the week × their number). Print them all.

8. A shopkeeper stores the item name, price, and quantity in variables. Calculate the total cost and print a receipt-style output.

9. Create a variable `message` and assign it a sentence. Reassign the same variable three more times with different sentences. Print the value after each assignment to trace the changes.

10. Write a program using only constants (ALL_CAPS naming) to store your country name, capital city, and population. Print them in a descriptive paragraph.
