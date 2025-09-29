release: python manage.py collectstatic --noinput
web: gunicorn ecommestore.wsgi:application --chdir src --bind 0.0.0.0:$PORT