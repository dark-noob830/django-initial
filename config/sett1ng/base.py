from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
env = os.environ.get

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Debug mode settings
DEBUG = env("DEBUG").lower() == "true"

# Deployment environment settings

deploy = env("deploy").lower() == "true"
# Secret key for security purposes
SECRET_KEY = env("SECRET_KEY")


REDIS_LINK = env("REDIS_LINK")
RABBIT_URI = env("RABBIT_URI")


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

