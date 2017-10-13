# Python imports

# Core Flask imports

# Third-Party imports
from elasticsearch import Elasticsearch
# Apps Imports
from config import (
	ELASTICSEARCH_HOST, 
	ELASTICSEARCH_PORT,
	ELASTICSEARCH_INDEX_NAME,
)


class ElasticSearchHandler(object):

	client = None
	index_name = ELASTICSEARCH_INDEX_NAME 

	def __new__(self):
		if not self.client:
			self.client = Elasticsearch([{
				'host': ELASTICSEARCH_HOST, 
				'port': ELASTICSEARCH_PORT
			}])
		return self