#!/usr/bin/env python3
"""defines checking of type"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """defines zooned array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in)
