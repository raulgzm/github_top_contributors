# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app.github.connector import GithubConnSingleton

def get_github_users_by_location(location):
	github_handler = GithubConnSingleton()
	user_paginated_list = github_handler.search_users(
		query='', 
		**{'location': 'barcelona'}
	)
	for user in user_paginated_list:
		yield user