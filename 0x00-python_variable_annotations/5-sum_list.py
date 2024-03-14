#!/usr/bin/env python3

"""
Implementation of Static typing of Python
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of list of float elements
    """
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
