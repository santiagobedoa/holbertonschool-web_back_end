#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that takes a list of ints and floats
    and return it sum
    """
    return sum(mxd_lst)
