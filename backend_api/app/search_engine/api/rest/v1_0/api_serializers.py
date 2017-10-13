# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports


class GithubUserSerializer(object):

	total = 0
	hits = []
	results = None

	def __init__(self, total, hits):
		self.total = total
		self.hits = hits

	def get_results(self):
		self.results = []
		for hit in self.hits:
			self.results.append({
				'username': hit['_source']['username'],
				'user_id': hit['_source']['user_id'],
				'repositories': hit['_source']['repositories'],
				'location': hit['_source']['location'],
				'user_profile_page': hit['_source']['user_profile_page'],
				'contributions': hit['_source']['contributions'],
			})
		return self.results

	def to_representation(self):
		return {
			'count': self.total,
			'results': self.get_results()
		}

	@property
	def data(self):
		return self.to_representation()