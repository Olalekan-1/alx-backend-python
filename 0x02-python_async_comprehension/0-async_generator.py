#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
from typing import Generator
import asyncio as a
import random as rd


async def async_generator() -> Generator[float]:
    """ Async generator """
    for _ in range(10):
        await a.sleep(1)
        yield rd.uniform(0, 10)
