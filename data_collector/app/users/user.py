# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports


class User(object):
	user_id = None
	username = ""
	location = ""
	contributions = 0

	def __init__(self, user_id, username, location, contributions):
		self.user_id = user_id
		self.username = username
		self.location = location
		self.contributions = contributions
