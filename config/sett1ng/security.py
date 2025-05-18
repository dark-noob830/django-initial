from .base import *

if DEBUG:

    CORS_ALLOW_ALL_ORIGINS = True
    ALLOWED_HOSTS = ["*"]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
else:
    CORS_ALLOWED_ORIGINS = [
        'http://127.0.0.1:5173',
        'http://localhost:5173',
        'https://batbooks-frontend.liara.run'
    ]
    ALLOWED_HOSTS = ['batbooks.ir', 'www.batbooks.ir', 'localhost', '127.0.0.1', '45.158.169.198', 'api']

    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_TRUSTED_ORIGINS = [
        'https://batbooks.ir',
        'https://www.batbooks.ir',

    ]

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
CORS_ALLOW_CREDENTIALS = False

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
