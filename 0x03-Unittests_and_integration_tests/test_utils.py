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
    def test_get_json(self):
        """Define test inputs"""
        test_cases = [
            ({"test_url": "http://example.com",
                "test_payload": {"payload": True}}),
            ({"test_url": "http://holberton.io",
                "test_payload": {"payload": False}}),
        ]

        for test_case in test_cases:
            test_url = test_case["test_url"]
            test_payload = test_case["test_payload"]
            with patch('utils.requests.get') as mock_requests_get:
                mock_response = Mock()
                mock_response.json.return_value = test_payload
                mock_requests_get.return_value = mock_response

                result = get_json(test_url)

                mock_requests_get.assert_called_once_with(test_url)
                self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
