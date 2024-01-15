#!/usr/bin/env python3
"""Executes multiple coroutines at the same time with async"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """defines multiple coroutines"""
    delays: List[float] = []
    total_delay: List[float] = []
    for x in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        first_result = await delay
        total_delay.append(first_result)
    return total_delay
