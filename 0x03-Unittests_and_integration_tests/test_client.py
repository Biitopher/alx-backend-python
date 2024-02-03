#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ Class test case githuborg client"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={'organization': 'mocked_org'})
    def test_org(self, org_name, mock_get_json):
        """Instantiate test org"""
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org

        mock_get_json.assert_called_once

        self.assertEqual(result, mock_get_json.return_value)

    def test_public_repos_url(self):
        """Set up a known payload to be returned by the org property"""

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            result = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(result,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock_get):
        """Defines public repos test"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/"
                          ) as mock_pub:
            test_client = GithubOrgClient("Test value")
            result = test_client.public_repos()

            self.assertEqual(result, ["Test value"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, return_value):
        """Defined licence test"""
        test_client = GithubOrgClient("Test value")
        result = test_client.has_license(repo, license_key)
        self.assertEqual(return_value, result)

@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                     "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class integration test"""
    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get"""
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Create an instance of GithubOrgClient"""
        result = GithubOrgClient("Test_value")
        self.assertTrue(result)
