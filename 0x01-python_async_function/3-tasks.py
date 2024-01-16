#!/usr/bin/env python3
"""Function that takes an integer delay and returns asyncio task"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """function wait_random in an asyncio task"""
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
