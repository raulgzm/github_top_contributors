# Python imports
import unittest
# Core Flask imports

# Third-Party imports
import mock
import requests
from requests.exceptions import HTTPError, MissingSchema
# Apps Imports
from app.scrappers.github_profile import GithubProfileScrapper
from app.scrappers.tests.mocks import (
	GITHUB_PROFILE_RESPONSE,
	GITHUB_PROFILE_HTML,
)


class GithubProfileScrapperTestSuite(unittest.TestCase):

	github_profile_mock = 'https://github.com/raulgonz'
	github_wrong_profile_mock = '//github.com/raulgonz'

	@mock.patch('requests.get')
	def test_read_profile_page(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 200
		mock_response.text = GITHUB_PROFILE_RESPONSE	
		mock_get.return_value = mock_response
		response = GithubProfileScrapper.read_profile_page(
			user_profile_page=self.github_profile_mock
		)
		self.assertGreater(len(response), 1)
		self.assertIn('<!DOCTYPE html>', response)
		self.assertIn('<body', response)

	@mock.patch('requests.get')
	def test_read_profile_page_empty_response(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 200
		mock_response.text = ""	
		mock_get.return_value = mock_response
		response = GithubProfileScrapper.read_profile_page(
			user_profile_page=self.github_profile_mock
		)
		self.assertEqual(len(response), 0)

	@mock.patch('requests.get')
	def test_read_profile_page_not_found(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 404
		mock_response.text = ""	
		mock_get.return_value = mock_response
		response = GithubProfileScrapper.read_profile_page(
			user_profile_page=self.github_profile_mock
		)
		self.assertEqual(len(response), 0)

	@mock.patch('requests.get')
	def test_read_profile_page_network_exception(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 500
		mock_response.raise_for_status.side_effect = HTTPError("Github is down")
		mock_get.return_value = mock_response
		response = GithubProfileScrapper.read_profile_page(
			user_profile_page=self.github_profile_mock
		)
		self.assertEqual(len(response), 0)

	@mock.patch('requests.get')
	def test_read_profile_page_invalid_url(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 500
		mock_response.raise_for_status.side_effect = MissingSchema("Invalid URL")
		mock_get.return_value = mock_response
		response = GithubProfileScrapper.read_profile_page(
			user_profile_page=self.github_wrong_profile_mock
		)
		self.assertEqual(len(response), 0)

	def test_find_contribution_element(self):
		contributions = GithubProfileScrapper.find_contribution_element(
			html_response=GITHUB_PROFILE_HTML
		)
		self.assertIn('10 contributions', contributions)

	def test_find_contribution_element_html_empty(self):
		contributions = GithubProfileScrapper.find_contribution_element(
			html_response=""
		)
		self.assertEqual(len(contributions), 0)

	@mock.patch('requests.get')
	def test_get_user_contributions(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 200
		mock_response.text = GITHUB_PROFILE_HTML	
		mock_get.return_value = mock_response
		contributions = GithubProfileScrapper.get_user_contributions(self.github_profile_mock)
		self.assertEqual(contributions, 10)

	@mock.patch('requests.get')
	def test_get_user_contributions_empty_response
	(self, mock_get):
		mock_response = mock.Mock()
		mock_response.status_code = 200
		mock_response.text = ""	
		mock_get.return_value = mock_response
		contributions = GithubProfileScrapper.get_user_contributions(self.github_profile_mock)
		self.assertEqual(contributions, 0)

if __name__ == '__main__':
    unittest.main()