# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports


class UserSerializer(object):

	user = None

	def __init__(self, user):
		self.user = user

	def to_representation(self):
		return self.user.__dict__

	@property
	def data(self):
		return self.to_representation()
