# Python imports

# Core Flask imports

# Third-Party imports
from elasticsearch import Elasticsearch
# Apps Imports
from app.settings.config import (
	ELASTICSEARCH_HOST, 
	ELASTICSEARCH_PORT,
	ELASTICSEARC_INDEX_NAME,
)


user_mapping = {
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 2
    },
    "user": {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "location": {"type": "string"},
            "contributions": {"type": "int"},
        }
    }
}

class ElasticSearchFactory(object):

	__instance = None
	index_name = ELASTICSEARC_INDEX_NAME

	def __new__(self):
		if not self.__instance:
			self.__instance = Elasticsearch([{
				'host': ELASTICSEARCH_HOST, 
				'port': ELASTICSEARCH_PORT
			}])
		self.init_idex()
		return self.__instance

	@classmethod
	def init_idex(cls):
		if not cls.__instance.indices.exists(cls.index_name):
			cls.__instance.indices.create(
                index=cls.index_name,
                body=user_mapping
            )