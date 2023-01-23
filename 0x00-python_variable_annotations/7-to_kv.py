#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """function that takes a str and a number and returns a tuple"""
    return (k, v * v)
