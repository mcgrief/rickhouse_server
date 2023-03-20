#!/bin/bash
rm -rf rickhouseapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations rickhouseapi
python3 manage.py migrate rickhouseapi
python3 manage.py loaddata user
python3 manage.py loaddata whiskey_type
python3 manage.py loaddata distillery
python3 manage.py loaddata whiskey
python3 manage.py loaddata whiskeydistillery
