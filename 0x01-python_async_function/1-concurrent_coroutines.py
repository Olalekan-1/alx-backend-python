#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
from typing import List


wait_random: any = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls wait_random() in n number times and return the
    list of random time generated
    """
    return_value: List[float] = []
    for _ in range(n):
        time: float = await wait_random(max_delay)
        return_value.append(time)
    return sorted(return_value)
