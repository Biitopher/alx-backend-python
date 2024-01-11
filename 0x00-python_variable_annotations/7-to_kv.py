#!/usr/bin/env python3
"""Returns a tuple where the first element is the string"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """defines tuple containing string"""
    return k, float(v ** 2)
