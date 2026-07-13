Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
# . .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "development"
$SqlitePath = (Join-Path $ProjectRoot "instance\app.db").Replace("\", "/")
$env:DATABASE_URL = "sqlite:///$SqlitePath"
$env:PYTHONPATH = $ProjectRoot

if (-not (Test-Path "instance")) {
    New-Item -ItemType Directory -Path "instance" | Out-Null
}

if (Test-Path "instance\app.db") {
    Remove-Item -Recurse -Force "instance\app.db"
}

python -m flask --app wsgi:app db upgrade
Write-Host "Local SQLite database reset and migrated."

