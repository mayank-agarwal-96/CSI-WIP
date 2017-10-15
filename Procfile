worker: python manage.py listen
web: gunicorn gocamping.wsgi --log-file -
worker: python manage.py celery worker -B -l info