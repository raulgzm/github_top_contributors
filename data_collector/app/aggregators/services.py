# Python imports

# Core Flask imports

# Third-Party imports
from github import RateLimitExceededException
# Apps Imports
from app.github.connector import GithubConnSingleton
from app.users.user import User


class AggregatorServices(object):

	@classmethod
	def create_user_from_github_user_class(cls, github_user):
		return User(
			user_id=github_user.id,
			username=github_user.name,
			location=github_user.location,
			contributions=0
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