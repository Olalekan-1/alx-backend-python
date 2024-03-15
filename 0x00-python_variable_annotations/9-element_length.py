#!/usr/bin/env python3

"""
Implementation of Static typing of Python
"""
from typing import Sequence, Tuple


def element_length(lst: Sequence[str]) -> Sequence[Tuple[str, int]]:
    """Returns a sequence of tuples"""
    return [(i, len(i)) for i in lst]
