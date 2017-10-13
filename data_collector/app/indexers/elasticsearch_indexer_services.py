# Python imports

# Core Flask imports

# Third-Party imports
from elasticsearch import helpers
# Apps Imports
from app.indexers.elastic_search_factory import ElasticSearchFactory
from app.settings.config import ELASTICSEARCH_INDEX_NAME, ELASTICSEARCH_DOC_TYPE

class ElasticSearchIndexerServices(object):

	@classmethod
	def __update_user_in_index(cls, user_id, user_serializer_data):
		client = ElasticSearchFactory()
		client.update(
			index=ELASTICSEARCH_INDEX_NAME,
			doc_type=ELASTICSEARCH_DOC_TYPE,
			id=user_id,
            body=user_serializer_data,
        )

	@classmethod
	def __create_user_in_index(cls, user_id, user_serializer_data):
		client = ElasticSearchFactory()
		client.index(
			index=ELASTICSEARCH_INDEX_NAME, 
			doc_type=ELASTICSEARCH_DOC_TYPE, 
			id=user_id, 
			body=user_serializer_data
		)

	@classmethod
	def index_user_in_elasticsearch(cls, user_id, user_serializer_data):
		cls.__create_user_in_index(user_id, user_serializer_data)

	@classmethod
	def make_index_document(cls, user_id, user_serializer_data):
		return {
			'_index': ELASTICSEARCH_INDEX_NAME,
			'_type': ELASTICSEARCH_DOC_TYPE,
			'id': user_id,
			'body': user_serializer_data,
		}

	@classmethod
	def index_users_in_bulk(cls, user_documents):
		client = ElasticSearchFactory()
		helpers.bulk(client, user_documents)