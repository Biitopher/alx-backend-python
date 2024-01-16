#!/usr/bin/env python3
"""coroutine collectrandom numbers using async and return random numbers"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine random numbers"""
    random_numbers = [_ async for _ in async_generator()]
    return random_numbers
