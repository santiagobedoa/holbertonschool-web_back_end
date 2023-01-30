#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.

    Args:
        page: Current page
        page_size: Total size of the page
    Return:
        tuple with the range start and end size page
    """
    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
