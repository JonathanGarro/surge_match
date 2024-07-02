from celery import shared_task
from datetime import datetime

@shared_task
def print_hello():
    print(f'Hello! The time is {datetime.now()}')