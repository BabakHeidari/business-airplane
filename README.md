# Business Flight Simulator

Phase 1 Flask scaffold for a production-minded business consulting MVP.

## Local setup without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
export FLASK_ENV=development
export DATABASE_URL=sqlite:///instance/app.db
flask --app wsgi:app db upgrade
python seed/demo.py
flask --app wsgi:app run
```

## Docker Compose setup

```bash
cp .env.example .env
docker compose up --build
```

In another terminal run migrations and seed data:

```bash
docker compose exec web flask --app wsgi:app db upgrade
docker compose exec web python seed/demo.py
```

## Migrations

Create a migration after model changes:

```bash
flask --app wsgi:app db migrate -m "describe change"
flask --app wsgi:app db upgrade
```

## Demo accounts

Both demo accounts use password `NorthstarDemo123!`.

- Owner: `owner@northstar.example`
- Consultant: `consultant@northstar.example`

## Quality checks

```bash
pytest
ruff check .
```
