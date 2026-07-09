Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot
. .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "development"
$env:DATABASE_URL = "sqlite:///instance/app.db"
$env:PYTHONPATH = $ProjectRoot

if (-not (Test-Path "instance")) {
    New-Item -ItemType Directory -Path "instance" | Out-Null
}

python -m flask --app wsgi:app db upgrade
python -m flask --app wsgi:app run

