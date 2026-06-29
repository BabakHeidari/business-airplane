Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
. .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"

if (Test-Path "instance\app.db") {
    Remove-Item -Recurse -Force "instance\app.db"
}

flask --app wsgi:app db upgrade
Write-Host "Local SQLite database reset and migrated."

