# Django ORM & Management Commands Lab

## Environment Setup

### Activate Virtual Environment (Windows)

```bat
hello_env\Scripts\activate
```

### Go to Project Directory

```bat
cd C:\Users\robotics\Desktop\codebase\hello_project
```

---

# Running Django Commands

Run a custom management command:

```bash
python manage.py <command_name>
```

Run development server:

```bash
python manage.py runserver
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Open Django shell:

```bash
python manage.py shell
```

Create admin user:

```bash
python manage.py createsuperuser
```

Show applied migrations:

```bash
python manage.py showmigrations
```

---

# Task 1 â€” Hello World Command

Expected Output

```text
Hello Django Developer
```

---

# Task 2 â€” Retrieve All Students

Incorrect

```python
Students.object.all()
```

Error

```text
AttributeError:
type object 'Students' has no attribute 'object'
```

Correct

```python
Students.objects.all()
```

Example Output

```python
<QuerySet [...]>
```

---

# Task 3 â€” Dictionary Syntax

Incorrect

```python
student = {
    "roll_number":12
    "department":"AI"
}
```

Error

```text
SyntaxError:
Perhaps you forgot a comma?
```

Correct

```python
student = {
    "roll_number":12,
    "full_name":"Rahat",
    "department":"AI",
    "year":1
}
```

---

# Task 4 â€” Print Dictionary

```python
print(student)
```

Output

```text
{
    'roll_number':12,
    'full_name':'Rahat',
    'department':'AI',
    'year':1
}
```

---

# Task 5 â€” Dictionary Keys, Values and Items

```python
print(student.keys())
print(student.values())
print(student.items())
```

Loop through dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

# Task 6 â€” Dictionary Unpacking

Incorrect

```python
print(**student)
```

Incorrect

```python
a, b, c, d = **student
```

Incorrect

```python
a, b, c, d = *student
```

Correct

```python
a, b, c, d = student
print(a, b, c, d)
```

Output

```text
roll_number full_name department year
```

---

# Task 7 â€” Add a Student

```python
new_student = {
    "roll_number":12,
    "full_name":"Rahat",
    "department":"AI",
    "year":1
}

print("Adding new student in db")
print("Added", new_student)
```

---

# Task 8 â€” Random Choice

Incorrect

```python
choice("CS", "GLG", "AI", "SE")
```

Correct

```python
choice(["CS", "GLG", "AI", "SE"])
```

---

# Task 9 â€” Generate Fake Student Data

```python
from faker import Faker
from random import randint, choice

fake = Faker()

student = {
    "roll_number": randint(1,100),
    "full_name": fake.name(),
    "department": choice(["AI","CS","SE","GLG"]),
    "year": randint(1,4)
}

print(student)
```

---

# Task 10 â€” Generate 100 Fake Students

```python
from faker import Faker
from random import randint, choice

fake = Faker()

for _ in range(100):
    student = {
        "roll_number": randint(1,100),
        "full_name": fake.name(),
        "department": choice(["AI","CS","SE","GLG"]),
        "year": randint(1,4)
    }

    print(student)
```

---

# Django ORM Commands

## Create Record

```python
Students.objects.create(
    roll_number=101,
    full_name="Ali Ahmed",
    department="AI",
    year=2
)
```

---

## Retrieve All Records

```python
Students.objects.all()
```

---

## First Record

```python
Students.objects.first()
```

---

## Last Record

```python
Students.objects.last()
```

---

## Count Records

```python
Students.objects.count()
```

---

## Get One Record

```python
Students.objects.get(id=1)
```

or

```python
Students.objects.get(roll_number=12)
```

---

## Filter Records

```python
Students.objects.filter(department="AI")
```

---

## Exclude Records

```python
Students.objects.exclude(department="AI")
```

---

## Order By

Ascending

```python
Students.objects.order_by("roll_number")
```

Descending

```python
Students.objects.order_by("-roll_number")
```

---

## Values

```python
Students.objects.values()
```

Specific Fields

```python
Students.objects.values(
    "roll_number",
    "full_name"
)
```

---

## Values List

```python
Students.objects.values_list()
```

Specific Fields

```python
Students.objects.values_list(
    "full_name",
    "department"
)
```

---

## Check Record Exists

```python
Students.objects.filter(
    department="AI"
).exists()
```

---

## Update Record

```python
student = Students.objects.get(id=1)

student.department = "CS"
student.save()
```

---

## Delete Record

```python
student = Students.objects.get(id=1)
student.delete()
```

---

## Bulk Create

```python
Students.objects.bulk_create([
    Students(
        roll_number=1,
        full_name="Ali",
        department="AI",
        year=1
    ),
    Students(
        roll_number=2,
        full_name="Ahmed",
        department="CS",
        year=2
    )
])
```

---

# Common Errors

## Incorrect

```python
Students.object.all()
```

Correct

```python
Students.objects.all()
```

---

## Incorrect Dictionary

```python
{
    "roll_number":12
    "department":"AI"
}
```

Correct

```python
{
    "roll_number":12,
    "department":"AI"
}
```

---

## Incorrect Random Choice

```python
choice("AI","CS","SE","GLG")
```

Correct

```python
choice(["AI","CS","SE","GLG"])
```

---

## Incorrect Print

```python
print(**student)
```

Correct

```python
print(student)
```

---

## Summary

Students should now be able to:

- Create custom Django management commands
- Use Django ORM to create, read, update, and delete records (CRUD)
- Query the database using `filter()`, `exclude()`, `get()`, `values()`, and `values_list()`
- Generate fake data using the Faker library
- Use Python dictionaries correctly
- Understand common syntax and runtime errors
- Debug Django ORM and Python code