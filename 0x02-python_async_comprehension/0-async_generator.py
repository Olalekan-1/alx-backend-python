#!/usr/bin/env python3
"""
Task 0 - Write a co-routine function called async_generator
Implementation of python Async function - Co-routine
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """ Async generator
    Generates 10 numbers at regular interval
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
