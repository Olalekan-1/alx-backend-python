#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
import random as rd
from typing import Generator


async def async_generator() -> Generator[float]:
    """ Async generator """
    for _ in range(10):
        await a.sleep(1)
        yield rd.uniform(0, 10)
