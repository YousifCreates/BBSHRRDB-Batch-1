# Lab Manual — Operators in Python
### Module 1 | Python Programming Fundamentals
### Topic 3 of 3: Operators

---

## Background

An **operator** is a symbol that performs an operation on one or more values (called operands). Python has several categories of operators:

### Arithmetic Operators
| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Comparison Operators
Return `True` or `False`.
| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

### Logical Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `x > 0 and x < 10` |
| `or` | At least one True | `x < 0 or x > 100` |
| `not` | Inverts the result | `not True` → `False` |

### Assignment Operators
| Operator | Equivalent |
|----------|------------|
| `x += 5` | `x = x + 5` |
| `x -= 5` | `x = x - 5` |
| `x *= 2` | `x = x * 2` |
| `x //= 2` | `x = x // 2` |
| `x **= 2` | `x = x ** 2` |

---

## Solved Tasks

---

### Task 1 — Arithmetic Operations

**Objective:** Use all arithmetic operators on two numbers.

```python
a = 17
b = 5

print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b}  = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

**Output:**
```
17 + 5  = 22
17 - 5  = 12
17 * 5  = 85
17 / 5  = 3.4
17 // 5 = 3
17 % 5  = 2
17 ** 5 = 1419857
```

---

### Task 2 — Comparison Operators

**Objective:** Compare two values and observe boolean results.

```python
x = 10
y = 20

print(f"x == y : {x == y}")
print(f"x != y : {x != y}")
print(f"x >  y : {x > y}")
print(f"x <  y : {x < y}")
print(f"x >= y : {x >= y}")
print(f"x <= y : {x <= y}")
```

**Output:**
```
x == y : False
x != y : True
x >  y : False
x <  y : True
x >= y : False
x <= y : True
```

---

### Task 3 — Logical Operators

**Objective:** Combine conditions using `and`, `or`, `not`.

```python
age = 20
has_id = True

# Both conditions must be True
can_enter = age >= 18 and has_id
print("Can enter club:", can_enter)

# At least one condition True
is_eligible = age < 15 or age > 60
print("Eligible for discount:", is_eligible)

# Negate a condition
is_minor = not (age >= 18)
print("Is minor:", is_minor)
```

**Output:**
```
Can enter club: True
Eligible for discount: False
Is minor: False
```

---

### Task 4 — Assignment Operators

**Objective:** Modify a variable in-place using compound assignment operators.

```python
score = 100
print("Start:", score)

score += 20
print("After += 20:", score)

score -= 10
print("After -= 10:", score)

score *= 2
print("After *= 2:", score)

score //= 3
print("After //= 3:", score)

score **= 2
print("After **= 2:", score)
```

**Output:**
```
Start: 100
After += 20: 120
After -= 10: 110
After *= 2: 220
After //= 3: 73
After **= 2: 5329
```

---

### Task 5 — Practical: Even or Odd Checker

**Objective:** Use the modulus operator to determine if a number is even or odd.

```python
numbers = [0, 1, 7, 14, 25, 100, -3]

for n in numbers:
    if n % 2 == 0:
        print(f"{n:4} → Even")
    else:
        print(f"{n:4} → Odd")
```

**Output:**
```
   0 → Even
   1 → Odd
   7 → Odd
  14 → Even
  25 → Odd
 100 → Even
  -3 → Odd
```

---

## Student Practice Tasks

Solve the following tasks on your own. No solutions are provided here — attempt each one independently.

1. Write a program that takes two numbers and prints the result of all seven arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`).

2. Calculate the area and perimeter of a rectangle using variables for length and width. Use only arithmetic operators.

3. Write a program that converts a temperature from Celsius to Fahrenheit. Formula: `F = (C * 9/5) + 32`. Test with `0`, `100`, and `37` degrees Celsius.

4. A student scored `marks = 73` out of 100. Use comparison operators to check if the student: passed (>= 50), got a distinction (>= 80), and failed (< 50). Print all three results.

5. Write a program that uses the modulus operator (`%`) to check if a number is divisible by both 3 and 5, only by 3, only by 5, or neither. Test with the numbers `15`, `9`, `10`, and `7`.

6. Given `x = 8` and `y = 3`, use logical operators to evaluate and print: `x > 5 and y > 5`, `x > 5 or y > 5`, and `not (x == y)`.

7. Write a bank balance simulator. Start with `balance = 5000`. Use `+=` to deposit `1500`, `−=` to withdraw `800`, and `*=` to apply a `1.05` interest multiplier. Print the balance after each step.

8. Use the exponentiation operator (`**`) to compute and print: 2 to the power of 10, the square root of 144 (hint: `144 ** 0.5`), and 3 cubed.

9. Write a program that uses only comparison and logical operators (no `if` statements) to determine whether a given year is a leap year. A year is a leap year if it is divisible by 4 but not 100, OR divisible by 400. Print `True` or `False`.

10. Combine all operator types in one program: start with a number, apply arithmetic to transform it, compare it to a threshold, and use a logical operator to combine two comparison results into a final boolean output. Print each step.
