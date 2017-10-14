# Python imports

# Core Flask imports

# Third-Party imports
from celery import shared_task
# Apps Imports
from app.aggregators.services import AggregatorServices
from app.settings.config import LOCATIONS_ENABLED

@shared_task(name="run_github_users_aggregator")
def run_github_users_aggregator():
    AggregatorServices.run_github_aggregator(location=LOCATIONS_ENABLED[0])

@shared_task(name="index_user_contributions")
def index_user_contributions(user_id, user_profile_page, user_serializer_data):
	AggregatorServices.index_user_contributions(
		user_id=user_id, 
		user_profile_page=user_profile_page, 
		user_serializer_data=user_serializer_data
	)
