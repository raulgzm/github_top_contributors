# Python imports
import unittest
# Core Flask imports

# Third-Party imports

# Apps Imports
from app.users.user import User


class UserModelTestSuite(unittest.TestCase):

	def setUp(self):
		pass

	def test_create_user(self):
		user = User(user_id=1, username='haku', location='barcelona', contributions=0)
		self.assertIsInstance(user, User)
		self.assertEqual(user.id, 1)
		self.assertEqual(user.username, 'haku')
		self.assertEqual(user.location, 'barcelona')
		self.assertEqual(user.contributions, 0)

if __name__ == '__main__':
    unittest.main()
