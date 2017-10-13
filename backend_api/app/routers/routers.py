# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from app.search_engine.api.rest.v1_0.api_routers import SearchEngineRouter


class Router(object):

	def __init__(self, api):
		SearchEngineRouter.init_search_engine_routes(api)