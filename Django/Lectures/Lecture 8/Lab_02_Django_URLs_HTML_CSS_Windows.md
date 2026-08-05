# Lab Manual 02: Django URLs with HTML & CSS (Windows)

**Course:** Django Web Development\
**Lab Title:** Creating Web Pages Using Django URLs, HTML, and CSS

------------------------------------------------------------------------

# Objective

In this lab you will:

-   Create a Django project
-   Create a Django application
-   Configure Django URLs
-   Create HTML templates
-   Create a CSS stylesheet
-   Connect HTML pages with Django views
-   Display styled pages in the browser

------------------------------------------------------------------------

# Step 1: Create the Project

``` cmd
mkdir DjangoWebsite
cd DjangoWebsite

python -m venv venv

venv\Scripts\activate

pip install django

django-admin startproject myproject

cd myproject

python manage.py startapp website
```

------------------------------------------------------------------------

# Step 2: Register the App

Open **myproject/settings.py**

``` python
INSTALLED_APPS = [
    ...
    "website",
]
```

------------------------------------------------------------------------

# Step 3: Create Template and Static Folders

Create the following structure.

``` text
website/
│
├── templates/
│   └── website/
│       ├── home.html
│       ├── about.html
│       └── contact.html
│
├── static/
│   └── website/
│       └── style.css
│
├── views.py
└── urls.py
```

------------------------------------------------------------------------

# Step 4: Configure Templates

Open **myproject/settings.py**

Find:

``` python
'DIRS': [],
```

Replace with:

``` python
'DIRS': [],
```

> Django can automatically discover templates inside each app when
> `APP_DIRS=True` (default).

------------------------------------------------------------------------

# Step 5: Create Views

**website/views.py**

``` python
from django.shortcuts import render

def home(request):
    return render(request, "website/home.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")
```

------------------------------------------------------------------------

# Step 6: Create App URLs

**website/urls.py**

``` python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
```

------------------------------------------------------------------------

# Step 7: Connect Project URLs

**myproject/urls.py**

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
]
```

------------------------------------------------------------------------

# Step 8: Create CSS

**website/static/website/style.css**

``` css
body{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    margin:0;
}

nav{
    background:#1f4e79;
    padding:15px;
}

nav a{
    color:white;
    text-decoration:none;
    margin-right:15px;
    font-weight:bold;
}

.container{
    width:80%;
    margin:40px auto;
    background:white;
    padding:25px;
    border-radius:8px;
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

h1{
    color:#1f4e79;
}

footer{
    text-align:center;
    padding:15px;
    margin-top:30px;
    color:#666;
}
```

------------------------------------------------------------------------

# Step 9: Create Home Page

**website/templates/website/home.html**

``` html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'website/style.css' %}">
</head>
<body>

<nav>
    <a href="/">Home</a>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
</nav>

<div class="container">
    <h1>Welcome</h1>
    <p>This is the Home Page created using Django.</p>
</div>

<footer>
    Django Lab Manual
</footer>

</body>
</html>
```

------------------------------------------------------------------------

# Step 10: Create About Page

**website/templates/website/about.html**

``` html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
    <link rel="stylesheet" href="{% static 'website/style.css' %}">
</head>
<body>

<nav>
    <a href="/">Home</a>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
</nav>

<div class="container">
    <h1>About Us</h1>
    <p>This page explains our Django website.</p>
</div>

<footer>
    Django Lab Manual
</footer>

</body>
</html>
```

------------------------------------------------------------------------

# Step 11: Create Contact Page

**website/templates/website/contact.html**

``` html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <link rel="stylesheet" href="{% static 'website/style.css' %}">
</head>
<body>

<nav>
    <a href="/">Home</a>
    <a href="/about/">About</a>
    <a href="/contact/">Contact</a>
</nav>

<div class="container">
    <h1>Contact</h1>
    <p>Email: info@example.com</p>
    <p>Phone: +92-300-1234567</p>
</div>

<footer>
    Django Lab Manual
</footer>

</body>
</html>
```

------------------------------------------------------------------------

# Step 12: Run the Server

``` cmd
python manage.py runserver
```

Open:

-   http://127.0.0.1:8000/
-   http://127.0.0.1:8000/about/
-   http://127.0.0.1:8000/contact/

------------------------------------------------------------------------

# Folder Structure

``` text
myproject/
│
├── manage.py
├── website/
│   ├── static/
│   │   └── website/
│   │       └── style.css
│   ├── templates/
│   │   └── website/
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   ├── urls.py
│   └── views.py
└── myproject/
    ├── settings.py
    └── urls.py
```

------------------------------------------------------------------------

# Practical Exercise

1.  Create a **Services** page.
2.  Create a **Gallery** page.
3.  Add both links to the navigation bar.
4.  Style them using the same CSS file.

------------------------------------------------------------------------

# Lab Outcome

Students can:

-   Create a Django project and app.
-   Configure URL routing.
-   Render HTML templates.
-   Use a shared CSS file with Django Static Files.
-   Build a simple multi-page website using Django.
