# Python imports

# Core Flask imports

# Third-Party imports
from celery import shared_task
# Apps Imports
from app.aggregators.services import AggregatorServices

@shared_task(name="run_github_users_aggregator")
def run_github_users_aggregator():
    AggregatorServices.run_github_aggregator(location='barcelona')
