Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot
. .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "development"
$SqlitePath = (Join-Path $ProjectRoot "instance\app.db").Replace("\", "/")
$env:DATABASE_URL = "sqlite:///$SqlitePath"
$env:PYTHONPATH = $ProjectRoot

if (-not (Test-Path "instance")) {
    New-Item -ItemType Directory -Path "instance" | Out-Null
}

python seed/demo.py

