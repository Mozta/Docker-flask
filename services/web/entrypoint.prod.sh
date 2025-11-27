#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started PROD"
fi

# Copy static files to the volume
echo "Copying static files..."
cp -r /home/app/web/static/* /home/app/web/project/static/

# Change to app user
su app

exec "$@"