# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports


class User(object):
	user_id = None
	username = ""
	location = ""
	repositories = 0
	contributions = 0
	user_profile_page = ""

	def __init__(self, user_id, username, location, contributions, repositories, user_profile_page):
		self.user_id = user_id
		self.username = username
		self.location = location
		self.contributions = contributions
		self.repositories = repositories
		self.user_profile_page = user_profile_page

	def set_user_contributions(contributions):
		self.contributions = contributions
