#!/usr/bin/env pyhton3
"""Measure the runtime"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutine").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Returns total time / n for wait_n() execution
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
