#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for an random time between th range of 0 to max_delay
    Return:
    The random time generated
    """
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
