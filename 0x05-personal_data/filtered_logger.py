#!/usr/bin/env python3
"""
Regex-ing
"""
from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns the log message obfuscated
    """
    for item in fields:
        message = re.sub(
            rf"{item}=.+?{separator}", f"{item}={redaction}{separator}", message
        )

    return message
