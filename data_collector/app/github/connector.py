# Python imports

# Core Flask imports

# Third-Party imports
from github import Github
# Apps Imports
from app.settings.config import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET

class GithubConnSingleton(object):

	__instance = None

	def __new__(self):
		if not self.__instance:
			self.__instance = Github(client_id=GITHUB_CLIENT_ID, client_secret=GITHUB_CLIENT_SECRET)
		return self.__instance
	