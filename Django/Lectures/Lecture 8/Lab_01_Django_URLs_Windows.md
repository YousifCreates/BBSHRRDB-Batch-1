# Lab Manual 01: Django URLs (Windows)

**Course:** Django Web Development\
**Lab Title:** Creating Your First Django Project and Understanding
URLs\
**Platform:** Windows 10/11\
**Prerequisites:** Python 3.10+ installed and added to PATH, VS Code
(recommended)

------------------------------------------------------------------------

# Lab Objectives

By the end of this lab, students will be able to:

-   Install Django in a virtual environment.
-   Create a Django project.
-   Understand the project structure.
-   Create Django views.
-   Configure Django URLs.
-   Run the development server.
-   Test URL routing.

------------------------------------------------------------------------

# Software Requirements

-   Windows 10 or Windows 11
-   Python 3.10 or later
-   Visual Studio Code
-   Command Prompt or PowerShell

------------------------------------------------------------------------

# Step 1: Create a Project Folder

Open **Command Prompt** and create a folder.

``` cmd
mkdir DjangoLab
cd DjangoLab
```

------------------------------------------------------------------------

# Step 2: Create a Virtual Environment

``` cmd
python -m venv venv
```

This creates a virtual environment named **venv**.

------------------------------------------------------------------------

# Step 3: Activate the Virtual Environment

### Command Prompt

``` cmd
venv\Scripts\activate
```

### PowerShell

``` powershell
venv\Scripts\Activate.ps1
```

After activation you should see:

``` text
(venv) C:\Users\Student\DjangoLab>
```

------------------------------------------------------------------------

# Step 4: Upgrade pip

``` cmd
python -m pip install --upgrade pip
```

------------------------------------------------------------------------

# Step 5: Install Django

``` cmd
pip install django
```

Verify installation:

``` cmd
django-admin --version
```

------------------------------------------------------------------------

# Step 6: Create a Django Project

``` cmd
django-admin startproject myproject
```

Move into the project folder:

``` cmd
cd myproject
```

------------------------------------------------------------------------

# Step 7: Project Structure

``` text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Important files:

-   **manage.py** -- Django management utility.
-   **settings.py** -- Project configuration.
-   **urls.py** -- URL routing.
-   **wsgi.py / asgi.py** -- Deployment entry points.

------------------------------------------------------------------------

# Step 8: Run the Development Server

``` cmd
python manage.py runserver
```

Open:

``` text
http://127.0.0.1:8000/
```

If everything is correct, Django's welcome page will appear.

Stop the server with:

``` text
CTRL + C
```

------------------------------------------------------------------------

# Step 9: Create an Application

``` cmd
python manage.py startapp website
```

Project structure now becomes:

``` text
myproject/
│
├── manage.py
├── website/
└── myproject/
```

------------------------------------------------------------------------

# Step 10: Register the App

Open:

``` text
myproject/settings.py
```

Add the app inside **INSTALLED_APPS**.

``` python
INSTALLED_APPS = [
    ...
    "website",
]
```

Save the file.

------------------------------------------------------------------------

# Step 11: Create Views

Open:

``` text
website/views.py
```

Replace its contents with:

``` python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse("This is the About Page.")

def contact(request):
    return HttpResponse("This is the Contact Page.")
```

------------------------------------------------------------------------

# Step 12: Create URLs for the App

Create a new file:

``` text
website/urls.py
```

Add:

``` python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
]
```

------------------------------------------------------------------------

# Step 13: Connect App URLs to Project URLs

Open:

``` text
myproject/urls.py
```

Replace with:

``` python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]
```

------------------------------------------------------------------------

# Step 14: Run the Server Again

``` cmd
python manage.py runserver
```

Visit:

``` text
http://127.0.0.1:8000/
```

Expected Output:

``` text
Welcome to the Home Page!
```

Visit:

``` text
http://127.0.0.1:8000/about/
```

Expected Output:

``` text
This is the About Page.
```

Visit:

``` text
http://127.0.0.1:8000/contact/
```

Expected Output:

``` text
This is the Contact Page.
```

------------------------------------------------------------------------

# How Django URL Routing Works

``` text
Browser
   │
   ▼
Requested URL
   │
   ▼
Project urls.py
   │
   ▼
App urls.py
   │
   ▼
View Function
   │
   ▼
HttpResponse
   │
   ▼
Browser
```

------------------------------------------------------------------------

# Understanding path()

Syntax:

``` python
path("url/", view_function)
```

Example:

``` python
path("about/", views.about)
```

Meaning:

-   User visits `/about/`
-   Django calls `views.about()`
-   The view returns a response to the browser.

------------------------------------------------------------------------

# Practical Exercise

1.  Create a new view named `services`.
2.  Return:

``` text
Our Services Page
```

3.  Create the URL:

``` text
/services/
```

4.  Test it in your browser.

------------------------------------------------------------------------

# Challenge Activity

Create these additional pages:

-   `/gallery/`
-   `/courses/`
-   `/team/`
-   `/faq/`

Each page should return a different message.

------------------------------------------------------------------------

# Viva Questions

1.  What is Django?
2.  What is a URL?
3.  What is URL routing?
4.  What is the purpose of `urls.py`?
5.  What does `path()` do?
6.  What is a View?
7.  What is `HttpResponse`?
8.  Why do we use a virtual environment?
9.  What command starts the Django server?
10. What happens if a URL is not found?

------------------------------------------------------------------------

# Lab Outcome

After completing this lab, students should be able to:

-   Create a Django project.
-   Create a Django app.
-   Configure URL routing.
-   Create view functions.
-   Connect project URLs with app URLs.
-   Run and test a Django web application successfully.
