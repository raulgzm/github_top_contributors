# Python imports

# Core Flask imports

# Third-Party imports
from github import RateLimitExceededException
# Apps Imports
from app.github.connector import GithubConnSingleton


class AggregatorServices(object):

	@classmethod
	def get_github_users_by_location(cls, location):
		try:
			github_handler = GithubConnSingleton()
			user_paginated_list = github_handler.search_users(
				query='', 
				**{'location': location}
			)
			for user in user_paginated_list:
				yield user
		except RateLimitExceededException:
			raise StopIteration()