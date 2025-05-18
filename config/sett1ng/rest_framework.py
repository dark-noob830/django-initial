from .base import *
from datetime import timedelta

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}

ACCESS_TOKEN_LIFETIME = env("ACCESS_TOKEN_LIFETIME", "00-00-01").split("-")
REFRESH_TOKEN_LIFETIME = env("REFRESH_TOKEN_LIFETIME", "00-00-10").split("-")

acces_kwargs = {
    "days": int(ACCESS_TOKEN_LIFETIME[0]),
    "hours": int(ACCESS_TOKEN_LIFETIME[1]),
    "minutes": int(ACCESS_TOKEN_LIFETIME[2]),
}

refresh_kwargs = {
    "days": int(REFRESH_TOKEN_LIFETIME[0]),
    "hours": int(REFRESH_TOKEN_LIFETIME[1]),
    "minutes": int(REFRESH_TOKEN_LIFETIME[2]),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(**acces_kwargs),
    "REFRESH_TOKEN_LIFETIME": timedelta(**refresh_kwargs),
}
