# Python imports

# Core Flask imports

# Third-Party imports
from flask_restful import Resource, reqparse
# Apps Imports
from app.search_engine.services import SearchEngineServices

class SearchEngineSearchAPIController(Resource):

    def get_page_size(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page_size', type=int, help='Page should be integer')
        args = parser.parse_args()
        page_size = args['page_size'] if (args['page_size'] and args['page_size'] > 0) else 1
        return page_size

    def get_location_query(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location', type=str, help='Location should be text')
        args = parser.parse_args()
        location = args['location'] if args['location'] else ''
        return location


    def get(self):
        page_size = self.get_page_size()
        location = self.get_location_query()
        SearchEngineServices.search_github_users_in_elasticsearch(
            page_size=page_size,
            location=location
        )
        return {'hello': 'world {} - {}'.format(location, page_size)}
