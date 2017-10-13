# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from .api_controllers import SearchEngineSearchAPIController

class SearchEngineRouter(object):

	@classmethod
	def init_search_engine_routes(cls, api):
		api.add_resource(SearchEngineSearchAPIController, '/api/v1_0/search/')
		return api