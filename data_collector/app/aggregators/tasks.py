# Python imports

# Core Flask imports

# Third-Party imports
from celery import shared_task
# Apps Imports

@shared_task(name="my_background_task")
def my_background_task():
    return 2 + 2
