# Python imports

# Core Flask imports

# Third-Party imports
import celery
# Apps Imports


@celery.task
def my_background_task():
    return 2 + 2
