#!/usr/bin/env python3
""" Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """Test the memoize"""
    def test_memoize(self):
        """Define a class with method and memoized property"""
        class TestClass:
            """Test class test"""
            def a_method(self):
                """Initialize the method"""
                return 42

            @memoize
            def a_property(self):
                """initialize the property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            test_instance.a_property
            test_instance.a_property
            mock_a_method.assert_called_once


if __name__ == '__main__':
    unittest.main()
