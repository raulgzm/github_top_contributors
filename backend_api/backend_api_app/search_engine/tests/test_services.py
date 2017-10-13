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


class SearchEngineServicesTestSuite(unittest.TestCase):

	@mock.patch('elasticsearch.Elasticsearch.search')
	def test_search_github_users_in_elasticsearch(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 200
		mock_response.text = ELASTICSEARCH_RESULT_RESPONSE	
		mock_get.return_value = mock_response
		assert False, mock_get


if __name__ == '__main__':
    unittest.main()