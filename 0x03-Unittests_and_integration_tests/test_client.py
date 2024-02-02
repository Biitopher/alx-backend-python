#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from unittest.mock import patch
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
