#!/usr/bin/env python3
"""4. Task"""
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    results = []
    promises = []
    for _ in range(0, n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: results.append(x.result()))
        promises.append(task)

    for promise in promises:
        await promise

    return results
