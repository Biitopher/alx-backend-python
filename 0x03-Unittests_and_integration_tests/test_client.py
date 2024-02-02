#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
