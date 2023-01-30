#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.

    @page: starting page
    @page_size: number of elements per page
    """
    start = 0 if page == 1 else (page * page_size) - page_size
    end = page_size if page == 1 else page * page_size

    return (start, end)
