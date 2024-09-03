from __future__ import absolute_import, unicode_literals
import os
from celery import Celery  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gallery.settings')

app = Celery('gallery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
