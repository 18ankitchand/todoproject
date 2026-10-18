# Todo Project

A Django application with account signup, signin, and task creation, editing, completion, and deletion.

## Run locally

Requires Python 3.12 or later.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/signin/ or create an account at http://127.0.0.1:8000/signup/.

Set the `DJANGO_SECRET_KEY` environment variable to a persistent secret for stable sessions. Otherwise, a temporary development key is generated at startup. The local SQLite database and environment files are excluded from Git.

This project uses development settings; configure it separately before production deployment.
