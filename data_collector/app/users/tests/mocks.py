# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app.users.user import User

USER_ID_MOCK = 1
USERNAME_MOCK = 'haku'
LOCATION_MOCK = 'barcelona'
CONTRIBUTIONS_MOCK = 0


def create_user_mock(user_id=USER_ID_MOCK, username=USERNAME_MOCK, location=LOCATION_MOCK, contributions=CONTRIBUTIONS_MOCK):
	return User(
		user_id=user_id, 
		username=username, 
		location=location, 
		contributions=contributions
	)