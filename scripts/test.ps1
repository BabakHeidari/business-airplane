Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot
. .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "testing"
$env:TEST_DATABASE_URL = "sqlite:///:memory:"
$env:PYTHONPATH = $ProjectRoot

python -m ruff check .
python -m pytest

