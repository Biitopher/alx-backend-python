#!/usr/bin/env python3
"""coroutine executing four times in parallel"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    initial_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()

    return (end - initial_time)
