#!/usr/bin/env python3
"""coroutine random numbers using async and return random numbers"""

import asyncio
import random
from typing import List


async def async_comprehension() -> List[float]:
    """coroutine random numbers"""
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
