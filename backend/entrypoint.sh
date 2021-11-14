#!/bin/sh

set -e

echo "Starting backend..."

if $MIGRATIONS = true; then
     # python manage.py flush --no-input
     python manage.py makemigrations || {
     echo "Failed to run makemigrations."
     exit 1
     }

     # Apply migrations.
     python manage.py migrate || {
     echo "Failed to run db migrations."
     exit 1
     }
fi

if $COLLECSTATICS = true; then
     python manage.py collectstatic --no-input --clear || {
          echo "Failed to collect static files."
          exit 1
     }
fi

chown -R appuser /opt/app

# Now run everything else as a non-root user
gosu appuser /bin/bash

exec "$@"