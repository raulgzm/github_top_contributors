# Python imports

# Core Flask imports

# Third-Party imports
from github import RateLimitExceededException
# Apps Imports
from app.github.connector import GithubConnSingleton
from app.users.user import User
from app.users.serializers import UserSerializer
from app.indexers.elasticsearch_indexer_services import ElasticSearchIndexerServices
from app.scrappers.github_profile import GithubProfileScrapper
from app import celery


class AggregatorServices(object):

	@classmethod
	def create_user_from_github_user_class(cls, github_user):
		return User(
			user_id=github_user.id,
			username=github_user.name,
			location=github_user.location,
			contributions=0,
			repositories=github_user.public_repos,
			user_profile_page=github_user.html_url
		)

	@classmethod
	def build_user_document(cls, github_user):
		user = cls.create_user_from_github_user_class(github_user=github_user)
		return ElasticSearchIndexerServices.make_index_document(
			user_id=user.user_id,
			user_serializer_data=UserSerializer(user).data
		)

	@classmethod
	def get_github_users_by_location(cls, location):
		try:
			github_handler = GithubConnSingleton()
			github_users_paginated_list = github_handler.search_users(
				query='', 
				**{'location': location}
			)
			for github_user in github_users_paginated_list:
				yield cls.create_user_from_github_user_class(github_user=github_user)
		except RateLimitExceededException:
			raise StopIteration()

	@classmethod
	def run_github_aggregator(cls, location):
		for user in cls.get_github_users_by_location(location=location):
			ElasticSearchIndexerServices.index_user_in_elasticsearch(
				user_id=user.user_id,
				user_serializer_data=UserSerializer(user).data
			)
			celery.send_task(
				"index_user_contributions", 
				[user.user_id, user.user_profile_page, UserSerializer(user).data]
			)

	@classmethod
	def index_user_contributions(cls, user_id, user_profile_page, user_serializer_data):
		contributions = GithubProfileScrapper.get_user_contributions(
			user_profile_page=user_profile_page
		)
		user_serializer_data['contributions'] = contributions
		ElasticSearchIndexerServices.index_user_in_elasticsearch(
			user_id=user_id,
			user_serializer_data=user_serializer_data
		)
