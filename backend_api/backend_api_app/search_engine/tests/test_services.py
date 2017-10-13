# Python imports
import unittest
# Core Flask imports

# Third-Party imports
import mock
from elasticsearch import Elasticsearch
# Apps Imports
from backend_api_app.search_engine.tests.mocks import (
	ELASTICSEARCH_RESULT_RESPONSE,
)
from backend_api_app.search_engine.services import SearchEngineServices


class SearchEngineServicesTestSuite(unittest.TestCase):

	@mock.patch('elasticsearch.Elasticsearch.search')
	def test_search_github_users_in_elasticsearch(self, mock_get):
		mock_get.return_value = ELASTICSEARCH_RESULT_RESPONSE
		total, hits = SearchEngineServices.search_github_users_in_elasticsearch(
			location='barcelona',
			page_size=5
		)
		self.assertEqual(total, 1021)
		self.assertEqual(len(hits), 5)

if __name__ == '__main__':
    unittest.main()