# Python imports
import unittest
# Core Flask imports

# Third-Party imports

# Apps Imports
from app.indexers.elastic_search_factory import ElasticSearchFactory


class ElasticSearchFactoryTestSuite(unittest.TestCase):

	def test_singleton(self):
		first_client_es = ElasticSearchFactory()
		second_client_es = ElasticSearchFactory()
		self.assertIs(first_client_es, second_client_es)

if __name__ == '__main__':
    unittest.main()
