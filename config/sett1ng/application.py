from .base import *

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Local apps
INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'home.apps.HomeConfig',
    'book.apps.BookConfig',
    'user_info.apps.UserInfoConfig',
    'comments.apps.CommentsConfig',
    'book_actions.apps.BookActionsConfig',
    'tag.apps.TagConfig',
    'forum.apps.ForumConfig',
    'adv_search.apps.AdvSearchConfig',
    'chat.apps.ChatConfig',
]

# Third-Party Apps
INSTALLED_APPS += [
    'rest_framework',
    'debug_toolbar',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'channels',
    'drf_spectacular',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "config.asgi.application"

AUTH_USER_MODEL = "accounts.User"
