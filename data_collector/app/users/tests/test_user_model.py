# Python imports
import unittest
# Core Flask imports

# Third-Party imports

# Apps Imports
from app.users.user import User
from app.users.tests.mocks import (
	create_user_mock,
	USER_ID_MOCK,
	USERNAME_MOCK,
	LOCATION_MOCK,
	CONTRIBUTIONS_MOCK,
)


class UserModelTestSuite(unittest.TestCase):

	def test_create_user(self):
		user = create_user_mock()
		self.assertIsInstance(user, User)
		self.assertEqual(user.id, USER_ID_MOCK)
		self.assertEqual(user.username, USERNAME_MOCK)
		self.assertEqual(user.location, LOCATION_MOCK)
		self.assertEqual(user.contributions, CONTRIBUTIONS_MOCK)

if __name__ == '__main__':
    unittest.main()
