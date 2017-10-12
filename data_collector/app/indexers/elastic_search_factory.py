# Python imports

# Core Flask imports

# Third-Party imports
from elasticsearch import Elasticsearch
# Apps Imports
from app.settings.config import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT


class ElasticSearchFactory(object):

	__instance = None

	def __new__(self):
		if not self.__instance:
			self.__instance = Elasticsearch([{
				'host': ELASTICSEARCH_HOST, 
				'port': ELASTICSEARCH_PORT
			}])
		return self.__instance