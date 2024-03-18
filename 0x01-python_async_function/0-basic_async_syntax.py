#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
import random as rd


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for an random time between th range of 0 to max_delay
    """
    time = rd.uniform(0, max_delay)
    await a.sleep(time)
    return time
