#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
from typing import List


wait_random: any = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> any:
    """Create and return an asyncio.Task for wait_random(max_delay)."""
    return a.create_task(wait_random(max_delay))
