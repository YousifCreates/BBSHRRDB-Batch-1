# Solutions Manual
## Topic: Control Instructions — Conditional Statements

> This document contains solutions to all 12 student practice problems from the Lab Manual.  
> **For instructor / self-review use only.**

---

### Solution 1 — Positive, Negative, or Zero

```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

**Notes:** Using `float` handles decimal inputs as well.

---

### Solution 2 — Shop Discount

```python
bill = float(input("Enter bill amount (Rs.): "))

if bill > 5000:
    discount = 0.15
elif bill >= 2000:
    discount = 0.05
else:
    discount = 0

final = bill - (bill * discount)
print(f"Final amount after discount: Rs. {final:.2f}")
```

**Notes:** `:.2f` formats the output to two decimal places.

---

### Solution 3 — Largest of Three Numbers

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")
```

**Notes:** The `>=` (instead of `>`) handles ties gracefully — either tied value is a valid answer.

---

### Solution 4 — Vowel or Consonant

```python
char = input("Enter a single lowercase letter: ")

if char in ('a', 'e', 'i', 'o', 'u'):
    print(f"'{char}' is a Vowel")
else:
    print(f"'{char}' is a Consonant")
```

**Notes:** The `in` operator checks membership in a tuple, which is cleaner than chaining `or` conditions.

---

### Solution 5 — Traffic Light

```python
color = input("Enter traffic light color (red/yellow/green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
```

**Notes:** `.lower()` makes the check case-insensitive — `"Red"` and `"RED"` both work.

---

### Solution 6 — Triangle Classification

```python
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
```

**Notes:** `a == b == c` is valid chained comparison in Python. Equilateral must be checked before isosceles, otherwise an equilateral triangle would also match the isosceles condition.

---

### Solution 7 — Cinema Ticket Pricing

```python
age = int(input("Enter age: "))
student_card = input("Do you have a student card? (yes/no): ").lower()

if age < 12:
    print("Ticket price: Rs. 200")
elif age <= 25 and student_card == "yes":
    print("Ticket price: Rs. 350")
else:
    print("Ticket price: Rs. 500")
```

**Notes:** A 26-year-old with a student card still pays the adult price since the student discount requires `age <= 25`.

---

### Solution 8 — Days in a Month

```python
year  = int(input("Enter year: "))
month = int(input("Enter month number (1-12): "))

# Determine leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
elif month == 2:
    days = 29 if leap else 28
else:
    print("Invalid month number")
    days = None

if days is not None:
    print(f"Number of days: {days}")
```

**Notes:** The leap year logic is reused from Task 5 of the lab manual. The `in` operator cleanly replaces a long chain of `or` comparisons.

---

### Solution 9 — University Admission

```python
fsc = float(input("Enter FSc percentage: "))
entry = int(input("Enter entry test score (out of 100): "))

fsc_ok    = fsc >= 60
entry_ok  = entry >= 50

if fsc_ok and entry_ok:
    print("Admission Accepted")
elif fsc_ok and not entry_ok:
    print("Admission Rejected: Entry test score too low (minimum 50 required)")
elif not fsc_ok and entry_ok:
    print("Admission Rejected: FSc percentage too low (minimum 60% required)")
else:
    print("Admission Rejected: Both FSc percentage and entry test score are below requirement")
```

**Notes:** Storing the boolean results in variables (`fsc_ok`, `entry_ok`) before the conditionals makes the logic much easier to read.

---

### Solution 10 — Simple Calculator

```python
num1 = float(input("Enter first number: "))
op   = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(f"Result: {num1 + num2}")
elif op == '-':
    print(f"Result: {num1 - num2}")
elif op == '*':
    print(f"Result: {num1 * num2}")
elif op == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid operator")
```

**Notes:** Division by zero is handled with a nested `if` inside the `/` branch — this is a classic use of nested conditionals for targeted error handling.

---

### Solution 11 — BMI Classification

```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
```

**Notes:** `**` is Python's exponentiation operator. Like the grade classifier in Task 3, cascading `<` checks are sufficient — no need for range expressions.

---

### Solution 12 — Number Guessing Hint

```python
secret = int(input("Enter the secret number (1-100): "))
guess  = int(input("Enter your guess: "))

if guess > secret:
    print("Too High")
elif guess < secret:
    print("Too Low")
else:
    print("Correct!")
```

**Notes:** This is the logic core of a full number guessing game. Wrapping it in a `while` loop (a future topic) would allow repeated guessing until the user is correct.

---

*— End of Solutions Manual —*
