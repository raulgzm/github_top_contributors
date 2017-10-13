# Python imports

# Core Flask imports

# Third-Party imports
import requests
from bs4 import BeautifulSoup
# Apps Imports


class GithubProfileScrapper(object):

	contributions_xpath = '#js-pjax-container > div > div.col-9.float-left.pl-2 > div.position-relative > div.mt-4 > div.js-contribution-graph > h2'

	@classmethod
	def read_profile_page(cls, user_profile_page):
		try:
			response = requests.get(user_profile_page)
			if response.status_code == 200:
				return response.text
			return ''
		except Exception:
			return ''

	@classmethod
	def find_contribution_element(cls, html_response):
		soup = BeautifulSoup(html_response, "lxml")
		contributions = soup.select(cls.contributions_xpath)
		if contributions:
			return BeautifulSoup(str(contributions[0])).text
		return ''



	@classmethod
	def get_user_contributions(cls, user_profile_page):
		response = cls.read_profile_page(user_profile_page)
		contributions = cls.find_contribution_element(html_response=response)
		if contributions:
			number_of_contributions = [int(s) for s in contributions.split() if s.isdigit()]
			if number_of_contributions:
				return number_of_contributions[0]
		return 0
