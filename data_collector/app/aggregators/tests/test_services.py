# Python imports
import unittest
# Core Flask imports

# Third-Party imports
import mock
# Apps Imports
from app.aggregators.services import AggregatorServices
from app.users.user import User


class AggregatorsServicesTestSuite(unittest.TestCase):

	def setUp(self):
		self.aggregator = AggregatorServices()

	def test_get_github_users_by_location(self):
		user_generator = self.aggregator.get_github_users_by_location(location='barcelona')
		self.assertIsInstance(next(user_generator), User)

	def test_get_github_users_by_location_stop_iteration(self):
		with mock.patch('app.aggregators.services.AggregatorServices.get_github_users_by_location') as mock_get:
			mock_get.side_effect=StopIteration()
			with self.assertRaises(StopIteration):
				self.aggregator.get_github_users_by_location(location='barcelona')

if __name__ == '__main__':
    unittest.main()