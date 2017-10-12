# Python imports
import unittest
# Core Flask imports

# Third-Party imports

# Apps Imports
from app.users.user import User
from app.users.serializers import UserSerializer
from app.users.tests.mocks import (
	create_user_mock,
	USER_ID_MOCK,
	USERNAME_MOCK,
	LOCATION_MOCK,
	CONTRIBUTIONS_MOCK,
)


class UserSerializersTestSuite(unittest.TestCase):

	def test_user_serializer(self):
		user = create_user_mock()
		user_serializer = UserSerializer(user=user)
		user_dict = user_serializer.to_representation()
		self.assertIn('user_id', user_dict)
		self.assertIn('username', user_dict)
		self.assertIn('location', user_dict)
		self.assertIn('contributions', user_dict)
		self.assertEqual(user_dict['user_id'], USER_ID_MOCK)
		self.assertEqual(user_dict['username'], USERNAME_MOCK)
		self.assertEqual(user_dict['location'], LOCATION_MOCK)
		self.assertEqual(user_dict['contributions'], CONTRIBUTIONS_MOCK)

	def test_user_serializer_data(self):
		user = create_user_mock()
		user_serializer = UserSerializer(user=user)
		user_dict = user_serializer.data
		self.assertIn('user_id', user_dict)
		self.assertIn('username', user_dict)
		self.assertIn('location', user_dict)
		self.assertIn('contributions', user_dict)
		self.assertEqual(user_dict['user_id'], USER_ID_MOCK)
		self.assertEqual(user_dict['username'], USERNAME_MOCK)
		self.assertEqual(user_dict['location'], LOCATION_MOCK)
		self.assertEqual(user_dict['contributions'], CONTRIBUTIONS_MOCK)


if __name__ == '__main__':
    unittest.main()
