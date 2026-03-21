#!/bin/sh
set -e

if [ "$APP_ENV" = "production" ]; then
    echo "🚀 Starting in PRODUCTION mode (Gunicorn)..."
    exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8010 --access-logfile - app.main:app
else
    echo "🛠️ Starting in DEVELOPMENT mode (Uvicorn Reload)..."
    exec uvicorn app.main:app --host 0.0.0.0 --port 8010 --reload
fi
