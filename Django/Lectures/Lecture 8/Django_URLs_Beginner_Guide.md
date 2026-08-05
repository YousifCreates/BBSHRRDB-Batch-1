# Django URLs Explained (Beginner-Friendly)

## What are Django URLs?

Think of **Django URLs as the GPS or road map of your website**. 🗺️

When someone types a web address (URL) into their browser, Django
decides **which Python function (called a view)** should handle that
request and what page to display.

For example:

``` text
https://example.com/
https://example.com/about/
https://example.com/contact/
```

Each URL should display a different page. Django uses **URL routing** to
connect each URL to the correct view.

------------------------------------------------------------------------

# Real-Life Analogy 🚗

Imagine a city:

-   **Road** → URL
-   **Traffic Police** → Django URL Dispatcher
-   **Destination (House/Shop)** → Django View

If someone travels on the road:

``` text
/about/
```

The traffic police directs them to the **About Page**.

Similarly, Django receives:

``` text
/about/
```

and sends the request to the appropriate Python function.

------------------------------------------------------------------------

# How Django URLs Work

``` text
User
 │
 ▼
Types a URL in the browser
 │
 ▼
Django URL Dispatcher
 │
 ▼
Matches a URL pattern
 │
 ▼
Calls the correct View
 │
 ▼
View prepares a response
 │
 ▼
Browser displays the page
```

------------------------------------------------------------------------

# The `urls.py` File

Every Django project contains a file named:

``` text
urls.py
```

This file stores all the URL routes for your application.

Example:

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
]
```

------------------------------------------------------------------------

# Understanding `path()`

The basic syntax is:

``` python
path("URL/", view_function)
```

Example:

``` python
path("blog/", views.blog)
```

This means:

-   If a user visits:

``` text
http://127.0.0.1:8000/blog/
```

-   Django will execute:

``` python
views.blog()
```

------------------------------------------------------------------------

# Understanding Each URL

## Home Page

``` python
path('', views.home)
```

URL:

``` text
http://127.0.0.1:8000/
```

Runs:

``` python
views.home()
```

------------------------------------------------------------------------

## About Page

``` python
path('about/', views.about)
```

URL:

``` text
http://127.0.0.1:8000/about/
```

Runs:

``` python
views.about()
```

------------------------------------------------------------------------

## Contact Page

``` python
path('contact/', views.contact)
```

URL:

``` text
http://127.0.0.1:8000/contact/
```

Runs:

``` python
views.contact()
```

------------------------------------------------------------------------

# What Happens if the URL Doesn't Exist?

Suppose a user visits:

``` text
http://127.0.0.1:8000/abc/
```

But your project does not contain:

``` python
path("abc/", ...)
```

Django cannot find a matching route, so it returns:

``` text
404 Page Not Found
```

------------------------------------------------------------------------

# Another Easy Analogy ☎️

Think of Django as a telephone operator.

  Number Dialed   Connected To
  --------------- -----------------
  100             Police
  101             Fire Department

Similarly:

  URL           Django Calls
  ------------- --------------
  `/about/`     `about()`
  `/contact/`   `contact()`

------------------------------------------------------------------------

# Summary

-   A **URL** is the web address a user visits.
-   Django stores URL routes inside **`urls.py`**.
-   The **URL Dispatcher** checks every incoming request.
-   If a matching route exists, Django calls the correct **View**.
-   The **View** prepares a response (HTML, JSON, etc.).
-   If no route matches, Django returns a **404 Page Not Found** error.

> **In simple words:** Django URLs are like a map that tells Django
> **which Python function should run when someone visits a particular
> web address.**
