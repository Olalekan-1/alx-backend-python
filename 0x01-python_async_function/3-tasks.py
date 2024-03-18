#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a


wait_random: any = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> a.Task:
    """Create and return an asyncio.Task for wait_random(max_delay)."""
    loop = a.get_event_loop()
    return loop.create_task(wait_random(max_delay))
