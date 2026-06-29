# Business Flight Simulator

Phase 1 Flask scaffold for a production-minded business consulting MVP. The primary development target is **Windows 11 with PowerShell and Docker Desktop**.

## Prerequisites on Windows

Install these before setup:

- Python 3.12+
- Git for Windows
- Docker Desktop, if you want the PostgreSQL-backed Docker workflow
- Optional: PostgreSQL for Windows, only if you want to run PostgreSQL locally without Docker

If PowerShell blocks local scripts, run this in the current terminal session before running project scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Quick start on Windows without Docker

From the repository root in PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\setup.ps1
.\scripts\reset_db.ps1
.\scripts\seed_demo.ps1
.\scripts\run.ps1
```

Open <http://127.0.0.1:5000>.

## Manual Windows setup without Docker

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"
flask --app wsgi:app db upgrade
python seed/demo.py
flask --app wsgi:app run
```

The local non-Docker workflow uses SQLite at `instance/app.db`. SQLite is intended for local development convenience and automated tests only.

## Windows helper scripts

Run these from the repository root in PowerShell:

```powershell
.\scripts\setup.ps1       # Create .venv, install dependencies, create .env if missing
.\scripts\run.ps1         # Apply migrations and start Flask with local SQLite
.\scripts\test.ps1        # Run Ruff and Pytest
.\scripts\reset_db.ps1    # Remove local SQLite DB and re-run migrations
.\scripts\seed_demo.ps1   # Seed Northstar Coffee demo users and organization
```

## Docker Desktop workflow on Windows

The Docker workflow uses PostgreSQL in the `db` service. It uses relative bind mounts (`.:/app`) so it works from the repository root in PowerShell without Linux-only host paths.

Create your environment file:

```powershell
Copy-Item .env.example .env
```

Start the app and database:

```powershell
docker compose up --build
```

In a second PowerShell terminal, run migrations and seed data:

```powershell
docker compose exec web flask --app wsgi:app db upgrade
docker compose exec web python seed/demo.py
```

Useful Docker Desktop / PowerShell commands:

```powershell
docker compose ps
docker compose logs -f web
docker compose logs -f db
docker compose stop
docker compose start
docker compose down
docker compose up --build --force-recreate
```

Reset Docker PostgreSQL data when you intentionally want a clean database:

```powershell
docker compose down -v
docker compose up --build
```

Then re-run migrations and seed data:

```powershell
docker compose exec web flask --app wsgi:app db upgrade
docker compose exec web python seed/demo.py
```

## Migrations

Apply existing migrations locally with SQLite:

```powershell
.\.venv\Scripts\Activate.ps1
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"
flask --app wsgi:app db upgrade
```

Create a new migration after model changes:

```powershell
.\.venv\Scripts\Activate.ps1
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"
flask --app wsgi:app db migrate -m "describe change"
flask --app wsgi:app db upgrade
```

Run migrations in Docker against PostgreSQL:

```powershell
docker compose exec web flask --app wsgi:app db upgrade
```

## Running tests on Windows

```powershell
.\scripts\test.ps1
```

Or manually:

```powershell
.\.venv\Scripts\Activate.ps1
$env:FLASK_ENV = "testing"
$env:TEST_DATABASE_URL = "sqlite:///:memory:"
ruff check .
pytest
```

## Demo accounts

Both demo accounts use password `NorthstarDemo123!`.

- Owner: `owner@northstar.example`
- Consultant: `consultant@northstar.example`

## Optional Linux/macOS notes

Linux/macOS contributors can run equivalent commands using their shell of choice, but the maintained setup path for this repository is Windows PowerShell. Use the modern `docker compose` command rather than the legacy hyphenated Compose command.
