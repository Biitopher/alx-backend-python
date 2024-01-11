#!/usr/bin/env python3
"""Returns first element of list if non-empty, otherwise return None"""


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """defines first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
