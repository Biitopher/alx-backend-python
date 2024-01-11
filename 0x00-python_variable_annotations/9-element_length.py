#!/usr/bin/env python3
"""returns list of tuples where each tuple contains element"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """defines elements length"""
    return [(i, len(i)) for i in lst]
