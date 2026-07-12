Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
# . .\.venv\Scripts\Activate.ps1

$env:FLASK_ENV = "testing"
$env:TEST_DATABASE_URL = "sqlite:///:memory:"

ruff check .
pytest

