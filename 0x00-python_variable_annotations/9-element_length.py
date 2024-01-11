#!/usr/bin/env python3
"""returns list of tuples where each tuple contains element"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """defines elements length"""
    return [(i, len(i)) for i in lst]
