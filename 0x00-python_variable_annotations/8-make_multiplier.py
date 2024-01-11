#!/usr/bin/env python3
"""Returns a function that multiplies a float by a given multiplier"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """defines function multiplying float"""
    def multiplier_function(x: float) -> float:
        """defines multiplier function"""
        return x * multiplier

    return multiplier_function
