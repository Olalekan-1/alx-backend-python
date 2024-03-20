#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ runs coroutine in parallel
    """
    start = time()
    await a.gather(async_comprehension(), async_comprehension(),
                   async_comprehension(), async_comprehension())
    return time() - start
