# First create a new app

`python manage.py startapp [app_name] # myapp`

# Register the app in settings.py

Add name of created app `INSTALLED_APPS` list present in `settings.py` file 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... above are default apps 

    # ... below one is custom app
    'myapp',
]
```

# Write your model in app/models.py file

```python
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField(max_length=10)

```

# Write/Generate and Apply Migrations

`python manage.py makemigrations`

`python manage.py migrate`

# Register model as site in myapp/admin.py file

```python
from django.contrib import admin
from myapp.models import Person

# Register your models here.
admin.site.register(Person)
```

# For repersentation in admin use `__str__` method

```python
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name
```