#!/usr/bin/env python3
"""Calculates the sum of a list of integers and floats"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """defines sum of the input list elements"""
    return sum(mxd_lst)
