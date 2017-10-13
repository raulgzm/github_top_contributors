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
from backend_api_app.search_engine.api.rest.v1_0.api_serializers import GithubUserSerializer


class SearchEngineAPISerializersTestSuite(unittest.TestCase):

	@mock.patch('elasticsearch.Elasticsearch.search')
	def test_github_user_serializer(self, mock_get):
		mock_get.return_value = ELASTICSEARCH_RESULT_RESPONSE
		total, hits = SearchEngineServices.search_github_users_in_elasticsearch(
			location='barcelona',
			page_size=5
		)
		serializer = GithubUserSerializer(total=total, hits=hits)
		serializer_data = serializer.data
		self.assertIn('count', serializer_data)
		self.assertIn('results', serializer_data)
		self.assertEqual(serializer_data['count'], 1021)
		self.assertEqual(len(serializer_data['results']), 5)

if __name__ == '__main__':
    unittest.main()