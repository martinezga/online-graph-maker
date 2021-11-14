#!/bin/sh

set -e

echo "Starting backend..."

# # python manage.py flush --no-input
# python manage.py makemigrations || {
#     echo "Failed to run makemigrations."
#     exit 1
# }

# # Apply migrations.
# python manage.py migrate || {
#     echo "Failed to run db migrations."
#     exit 1
# }

python manage.py collectstatic --no-input --clear || {
     echo "Failed to collect static files."
     exit 1
}

exec "$@"