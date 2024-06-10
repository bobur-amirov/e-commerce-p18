import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.settings')

app = Celery('Ecommerce')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request}")


@app.task(bind=True)
def add(self, x, y):
    time.sleep(10)
    print(f"Adding {x} and {y}")
    return x + y


@app.task(bind=True)
def mul(self, x, y):
    time.sleep(5)
    print(f"Muling {x} and {y}")
    return x * y