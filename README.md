# Manual Django Web App

A small Django practice project that implements basic signup and login views using a custom user model.

## Features in the current code

- Signup form accepts a username, email and password
- Login view checks submitted credentials against the custom model
- Successful login renders a simple home template
- Django URL routes connect the signup and login views

## Tech stack

- Python
- Django
- HTML templates
- Django ORM with the configured database (SQLite by default unless settings are changed)

## Run locally

```bash
cd manual_model
python -m venv .venv
# Activate the environment, then:
pip install Django
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Project structure

- `manual_model/manage.py` — Django command-line entry point
- `manual_model/manual_model/` — project settings and root URL configuration
- `manual_model/account/` — custom user model, signup/login views and routes
- `manual_model/account/templetes/` — current HTML template directory (the spelling is retained to match the source code)

## Security note

This is an educational example, not production authentication. The current view/model code stores and compares passwords directly rather than using Django's password hashing and built-in authentication system. Do not deploy it or reuse real credentials without replacing that logic with Django's secure authentication APIs.
