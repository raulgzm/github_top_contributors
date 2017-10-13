# Python imports
import unittest
# Core Flask imports

# Third-Party imports

# Apps Imports
from app.github.connector import GithubConnSingleton


class ConnectorsTestSuite(unittest.TestCase):

	def test_singleton(self):
		first_handler = GithubConnSingleton()
		second_handler = GithubConnSingleton()
		self.assertIs(first_handler,  second_handler)


if __name__ == '__main__':
    unittest.main()