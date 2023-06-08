#!/usr/bin/env bash
pip install --upgrade pip
pip install poetry
#exit on error
set -o errexit

poetry install

poetry lock

python manage.py collectstatic --no-input
python manage.py migrate
