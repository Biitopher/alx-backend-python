#!/usr/bin/env python3
"""Safely gets the value associated with the given key in a dictionary"""


from typing import TypeVar, Any, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """defines value associated with key"""
    if key in dct:
        return dct[key]
    else:
        return default
