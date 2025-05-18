#!/bin/bash

set -e
chown -R appuser:appuser /app/media

echo ">> Running Migrations"
python manage.py migrate --noinput

echo ">> Collecting static files"
python manage.py collectstatic --noinput

exec su appuser -c "gunicorn config.asgi:application --bind 0.0.0.0:8000 --workers 2 --worker-class uvicorn.workers.UvicornWorker --max-requests 1000 --max-requests-jitter 50 --timeout 120 --graceful-timeout 120"

