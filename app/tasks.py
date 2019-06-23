from celery import shared_task

@shared_task
def hello():
    print("Welcome to fibonaci_api from celery")
