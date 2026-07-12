import os
from dataclasses import dataclass

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def _sqlite_uri_for_path(path: str) -> str:
    absolute_path = path if os.path.isabs(path) else os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(absolute_path), exist_ok=True)
    return f"sqlite:///{absolute_path.replace(os.sep, '/')}"


def _normalize_database_url(database_url: str | None, default_path: str) -> str:
    if not database_url:
        if default_path == ":memory:":
            return "sqlite:///:memory:"
        return _sqlite_uri_for_path(default_path)
    if database_url == "sqlite:///:memory:":
        return database_url
    if database_url.startswith("sqlite:///") and not database_url.startswith("sqlite:////"):
        return _sqlite_uri_for_path(database_url.removeprefix("sqlite:///"))
    return database_url


@dataclass
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-change-me")
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(os.getenv("DATABASE_URL"), "instance/app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = os.getenv("WTF_CSRF_ENABLED", "true").lower() == "true"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = SESSION_COOKIE_SECURE

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(os.getenv("TEST_DATABASE_URL"), ":memory:")

class ProductionConfig(Config):
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

config_by_name = {"development": DevelopmentConfig, "testing": TestingConfig, "production": ProductionConfig}
