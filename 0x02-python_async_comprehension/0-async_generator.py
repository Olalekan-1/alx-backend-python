#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
import random as rd
from typing import List


async def async_generator():
    """ Async generator """
    for _ in range(10):
        await a.sleep(1)
        yield rd.uniform(0, 10)
