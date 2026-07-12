Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
# . .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"

python seed/demo.py

