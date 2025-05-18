import dj_database_url
from .base import *

if deploy:
    DATABASES = {
        "default": dj_database_url.config(
            default=env("DATABASE_URL"),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }