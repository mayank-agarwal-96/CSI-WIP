web: gunicorn WIP.wsgi --log-file -
worker: python manage.py celery worker -B -l info & python manage.py listen