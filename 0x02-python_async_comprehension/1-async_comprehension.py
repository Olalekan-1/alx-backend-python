#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
from typing import Any


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Any:
    """ async comprhension"""
    async_numbers = [number async for number in async_generator()]
    return async_numbers
