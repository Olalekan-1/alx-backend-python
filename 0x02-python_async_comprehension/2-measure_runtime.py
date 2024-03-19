#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
from time import time
from typing import Any


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Any:
    """ runs coroutine in parallel
    """
    start = time()
    await a.gather(async_comprehension(), async_comprehension(),
                   async_comprehension(), async_comprehension())
    return time() - start
