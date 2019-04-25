import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freeze.settings')

app = Celery('freeze')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()