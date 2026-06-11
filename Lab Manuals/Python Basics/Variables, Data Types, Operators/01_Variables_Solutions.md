# Solutions — Variables in Python
### Module 1 | Python Programming Fundamentals
### Topic 1 of 3: Variables

---

> **Note for Instructors:** This file contains solutions to the 10 student practice tasks from the Variables Lab Manual. Distribute only after students have attempted the tasks independently.

---

### Solution 1 — Personal Variables

```python
full_name = "Yousif Ahmed"
age = 21
city = "Karachi"

print(full_name)
print(age)
print(city)
```

---

### Solution 2 — Swap Values

```python
a = 50
b = 80
print("Before:", a, b)

a, b = b, a
print("After:", a, b)
```

---

### Solution 3 — Counter Increment

```python
counter = 0
counter = counter + 1
counter = counter + 1
counter = counter + 1
counter = counter + 1
counter = counter + 1
print(counter)  # Output: 5
```

---

### Solution 4 — Memory Address with `id()`

```python
x = 5
y = 5
print(id(x))
print(id(y))
print(id(x) == id(y))  # Likely True for small integers (Python caches them)
```

> **Observation:** Python caches small integers (-5 to 256), so `x` and `y` point to the same object in memory. For larger numbers this would not be the case.

---

### Solution 5 — Type Change with Reassignment

```python
temperature = 36.6
print(temperature)        # 36.6

temperature = "Fever"
print(temperature)        # Fever
# Python allowed this — it's dynamically typed.
```

---

### Solution 6 — Formatted Student Info

```python
name = "Ali"
roll = 101
cgpa = 3.75

print(f"Student {name} (Roll: {roll}) has a CGPA of {cgpa}.")
```

---

### Solution 7 — Multiple Assignment in One Line

```python
mon, tue, wed, thu, fri = 1, 2, 3, 4, 5
print(mon, tue, wed, thu, fri)
```

---

### Solution 8 — Shopkeeper Receipt

```python
item = "Notebook"
price = 150
quantity = 4

total = price * quantity
print(f"Item: {item}")
print(f"Price per unit: Rs. {price}")
print(f"Quantity: {quantity}")
print(f"Total: Rs. {total}")
```

---

### Solution 9 — Tracing Reassignment

```python
message = "Hello!"
print(message)

message = "How are you?"
print(message)

message = "I am learning Python."
print(message)

message = "Variables are fun!"
print(message)
```

---

### Solution 10 — Constants

```python
COUNTRY = "Pakistan"
CAPITAL = "Islamabad"
POPULATION = 230_000_000

print(f"{COUNTRY} is a country in South Asia. Its capital is {CAPITAL} and it has a population of approximately {POPULATION} people.")
```
