#!/usr/bin/env python3
""" Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Class inheriting from unittest testcase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Access a nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception,
                                         expected_message):
        """Checks specified exception is raised fot given inputs"""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Call the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_response):
        """Define test inputs"""
        mock_response.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
