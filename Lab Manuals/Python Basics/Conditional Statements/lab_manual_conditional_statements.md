# Lab Manual
## Topic: Control Instructions — Conditional Statements
### Department of Computer Science

---

## Background

Control instructions direct the flow of a program. Without them, code executes line by line from top to bottom — but real programs need to make decisions. **Conditional statements** allow a program to choose between different paths of execution based on whether a condition evaluates to `True` or `False`.

### Key Concepts

**Boolean Expressions**  
A condition is any expression that resolves to `True` or `False`. Common comparison operators include:
- `==` (equal to), `!=` (not equal to)
- `<`, `>`, `<=`, `>=`

**Logical Operators**  
Multiple conditions can be combined using:
- `and` — both conditions must be true
- `or` — at least one condition must be true
- `not` — inverts the condition

**Types of Conditional Constructs**

| Construct | Purpose |
|---|---|
| `if` | Execute a block only if condition is True |
| `if-else` | Choose between two blocks |
| `if-elif-else` | Choose among multiple alternatives |
| Nested `if` | A conditional inside another conditional |

> **Note:** Python uses **indentation** (4 spaces) to define code blocks — there are no braces `{}` like in C/Java.

---

## Lab Tasks (With Solutions)

---

### Task 1 — Simple `if` Statement: Check Positive Number

**Objective:** Understand the basic `if` statement.

**Background:** The simplest conditional checks one condition. If the condition is `True`, the indented block runs; otherwise, Python skips it entirely.

**Problem:** Write a program that takes an integer input from the user and prints `"Positive number"` only if the number is greater than zero.

**Solution:**

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
```

**Sample Output:**
```
Enter a number: 7
Positive number
```

**Explanation:**  
- `int(input(...))` reads user input and converts it to an integer.  
- `if num > 0:` checks whether the value exceeds zero.  
- If the condition is `False` (e.g., input is `-3`), nothing is printed.

---

### Task 2 — `if-else` Statement: Even or Odd

**Objective:** Use `if-else` to handle two mutually exclusive outcomes.

**Background:** When exactly two outcomes are possible, `if-else` is the cleanest choice. The `else` block runs whenever the `if` condition is `False`.

**Problem:** Ask the user for an integer. Print `"Even"` if it is divisible by 2, otherwise print `"Odd"`.

**Solution:**

```python
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Sample Output:**
```
Enter an integer: 4
Even

Enter an integer: 9
Odd
```

**Explanation:**  
- The modulo operator `%` gives the remainder of division.  
- `num % 2 == 0` is `True` when there is no remainder, i.e., the number is even.

---

### Task 3 — `if-elif-else`: Grade Classification

**Objective:** Handle multiple ranges of values using `elif`.

**Background:** `elif` (short for "else if") lets you chain additional conditions. Python checks them in order and executes only the first block whose condition is `True`. The `else` at the end acts as a catch-all.

**Problem:** Read a numeric score (0–100) and print the letter grade according to the table below.

| Score Range | Grade |
|---|---|
| 90 – 100 | A |
| 80 – 89 | B |
| 70 – 79 | C |
| 60 – 69 | D |
| Below 60 | F |

**Solution:**

```python
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Sample Output:**
```
Enter your score (0-100): 85
Grade: B
```

**Explanation:**  
Because Python stops at the first `True` condition, we only need `>=` comparisons — we don't need to write `80 <= score < 90`.

---

### Task 4 — Nested `if`: Loan Eligibility

**Objective:** Use nested conditionals to evaluate multiple layered criteria.

**Background:** Sometimes a decision depends on a hierarchy of conditions — you only ask the second question if the first condition is already met. This is done by placing an `if` statement inside another `if` block.

**Problem:** A bank approves a loan if:
1. The applicant's age is at least 21, **and**
2. Their monthly salary is at least 30,000.

Print `"Loan Approved"` or an appropriate rejection reason.

**Solution:**

```python
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

if age >= 21:
    if salary >= 30000:
        print("Loan Approved")
    else:
        print("Loan Rejected: Salary too low")
else:
    print("Loan Rejected: Applicant must be at least 21 years old")
```

**Sample Output:**
```
Enter your age: 25
Enter your monthly salary: 25000
Loan Rejected: Salary too low
```

**Explanation:**  
The outer `if` gates access to salary checking. This structure gives a precise reason for each rejection, which `and` in a single condition cannot do alone.

---

### Task 5 — Logical Operators: Leap Year Checker

**Objective:** Combine multiple conditions using `and` / `or`.

**Background:** A year is a **leap year** if:
- It is divisible by 4, **and**
- It is **not** divisible by 100, **unless** it is also divisible by 400.

This rule requires combining `and`, `or`, and `not` (or their equivalents).

**Problem:** Take a year as input and print whether it is a leap year or not.

**Solution:**

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")
```

**Sample Output:**
```
Enter a year: 2000
2000 is a Leap Year

Enter a year: 1900
1900 is NOT a Leap Year
```

**Explanation:**  
- `2000 % 400 == 0` → True → Leap Year.  
- `1900 % 4 == 0` → True, but `1900 % 100 == 0` → the first part is False, and `1900 % 400 != 0` → overall False → Not a leap year.

---

## Student Practice Problems

> **Instructions:** Solve the following problems on your own. Write, run, and test your code. No solutions are provided here — refer to your solution sheet only after attempting each problem.

---

**Problem 1.**  
Write a program that takes a number as input and prints:
- `"Positive"` if the number is greater than 0
- `"Negative"` if the number is less than 0
- `"Zero"` if the number equals 0

---

**Problem 2.**  
A shop offers a 15% discount if a customer's bill exceeds Rs. 5,000, and a 5% discount if the bill is between Rs. 2,000 and Rs. 5,000 (inclusive). No discount is given otherwise. Take the bill amount as input and print the final amount after discount.

---

**Problem 3.**  
Take three numbers as input and print the largest among them using `if-elif-else`.

---

**Problem 4.**  
Write a program that checks whether a given character (input from the user) is a vowel (`a, e, i, o, u`) or a consonant. Assume the input is always a single lowercase letter.

---

**Problem 5.**  
A traffic light system uses colors: `"red"`, `"yellow"`, `"green"`. Take the color as input and print:
- `"Stop"` for red
- `"Get Ready"` for yellow
- `"Go"` for green
- `"Invalid color"` for anything else

---

**Problem 6.**  
Write a program that determines if a triangle is **equilateral**, **isosceles**, or **scalene** based on three side lengths entered by the user.

---

**Problem 7.**  
A cinema charges:
- Rs. 200 for children (age < 12)
- Rs. 350 for students (age 12–25 with a student card)
- Rs. 500 for adults

Take age and whether the person has a student card (`yes` / `no`) as inputs. Print the ticket price.

---

**Problem 8.**  
Write a program that reads a year and a month number (1–12) and prints the number of days in that month. Account for leap years in February.

---

**Problem 9.**  
A university admission system accepts students if:
- Their FSc marks are at least 60%, **and**
- Their entry test score is at least 50 out of 100.

If only one condition is met, print which requirement was not fulfilled. If neither is met, print both.

---

**Problem 10.**  
Write a simple calculator. Take two numbers and an operator (`+`, `-`, `*`, `/`) as input. Perform the corresponding operation and print the result. Handle division by zero with an appropriate message.

---

**Problem 11.**  
Write a program that takes a person's weight (kg) and height (m) as input, calculates their BMI (`BMI = weight / height²`), and classifies it as:
- Underweight: BMI < 18.5
- Normal: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obese: BMI ≥ 30

---

**Problem 12.**  
Write a number guessing hint program. Take a secret number (1–100) and a guessed number as input. Print:
- `"Too High"` if the guess is more than the secret number
- `"Too Low"` if the guess is less
- `"Correct!"` if they match

---

*— End of Lab Manual —*
