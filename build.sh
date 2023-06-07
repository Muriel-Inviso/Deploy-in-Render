#!/usr/bin/env bash

#exit on error
set -o errexit

poetry install
poetry self update
rm poetry.lock
poetry lock

python manage.py collectstatic --no-input
python manage.py migrate
