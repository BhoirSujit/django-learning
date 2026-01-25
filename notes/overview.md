# Django Overview

## What is Django?

Django is a high-level Python web framework that helps developers build web applications quickly and efficiently. It follows the **"batteries-included"** philosophy, which means it provides many built-in features like authentication, admin panel, and security.

Django is designed to make web development fast, secure, and scalable.

---

## Why Use Django?

Django is popular because it saves time and reduces complexity in web development.

### Key Benefits:

* 🚀 Fast Development
* 🔒 High Security
* 📈 Scalable
* 🧩 Built-in Admin Panel
* 🛠 Follows Best Practices
* ♻ Reusable Components

---

## Django Architecture (MVT Pattern)

Django follows the **MVT (Model-View-Template)** architecture.

### 1. Model

* Handles database structure
* Defines tables using Python classes
* Uses ORM (Object Relational Mapping)

### 2. View

* Contains business logic
* Processes requests and returns responses

### 3. Template

* Handles UI and presentation
* Uses HTML with Django template language

### Flow:

```
User → URL → View → Model → View → Template → Response
```

---

## Main Components of Django

### 1. Django ORM

* Connects Python code with databases
* Supports PostgreSQL, MySQL, SQLite, etc.
* No need to write complex SQL queries

### 2. Admin Panel

* Auto-generated admin interface
* Used to manage database data easily

### 3. Authentication System

* Login, Logout, Register
* Password management
* Permissions and Roles

### 4. URL Routing

* Maps URLs to views
* Makes app navigation easy

### 5. Middleware

* Handles requests and responses globally
* Used for security, sessions, logging, etc.

---

## Django Project vs Django App

### Django Project

* Main container of your website
* Contains settings and configurations

Example:

```
myproject/
```

### Django App

* Small module with specific functionality
* Example: blog, users, products

Example:

```
blog/
users/
```

One project can contain multiple apps.

---

## Basic Django Commands

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

Linux / Mac:

```bash
source env/bin/activate
```

### Install Django

```bash
pip install django
```

### Create Project

```bash
django-admin startproject myproject
```

### Run Server

```bash
cd myproject
python manage.py runserver
```

### Create App

```bash
python manage.py startapp myapp
```

---

## Project Folder Structure

After creating a project:

```
myproject/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── myapp/
```

---

## How Django Handles a Request

1. User sends a request from browser
2. Django checks `urls.py`
3. Calls the matching View
4. View interacts with Model (if needed)
5. Data is sent to Template
6. Final HTML response is returned

---

## Where Django is Used

Django is used by many big companies:

* Instagram
* Pinterest
* Mozilla
* Disqus
* Spotify

It is suitable for:

* Blogs
* E-commerce websites
* REST APIs
* Social Media Apps
* Admin Dashboards

---

## Django vs Other Frameworks

| Feature        | Django     | Flask  | Node.js |
| -------------- | ---------- | ------ | ------- |
| Type           | Full Stack | Micro  | Runtime |
| Learning       | Medium     | Easy   | Medium  |
| Built-in Tools | Many       | Few    | Depends |
| Security       | High       | Medium | Depends |

---

## Best Practices for Beginners

* Always use Virtual Environment
* Follow MVT Pattern
* Use GitHub for version control
* Write clean code
* Practice with projects

---

## Learning Roadmap

### Step 1: Basics

* Install Django
* Project setup
* URLs and Views

### Step 2: Database

* Models
* Migrations
* Admin Panel

### Step 3: Frontend

* Templates
* Static Files
* Forms

### Step 4: Advanced

* Authentication
* REST API (DRF)
* Deployment

---

