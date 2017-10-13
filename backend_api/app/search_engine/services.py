# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app.search_engine.elasticsearch_client import ElasticSearchHandler


class SearchEngineServices(object):

	@classmethod
	def search_github_users_in_elasticsearch(cls, location, page_size):
		 elastic_search_handler = ElasticSearchHandler()
		 results = elastic_search_handler.client.search(
		 	index=elastic_search_handler.index_name, 
		 	body={"size": page_size, "query": {"match": {"location": {"query": location, "type": "phrase"}}}}
		 )
		 assert False, results['hits']['hits']