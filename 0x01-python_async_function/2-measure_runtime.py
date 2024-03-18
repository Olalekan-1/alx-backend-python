#!/usr/bin/env python3

"""
Implementation of python Async function - Co-routine
"""
import asyncio as a
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ meassure the total tame of execution
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    # await asyncio.run(main())
    # task = await a.create_task(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
