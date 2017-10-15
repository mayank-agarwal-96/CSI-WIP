web: gunicorn gocamping.wsgi --log-file -
worker: python manage.py listen
worker: python manage.py celery worker -B -l info