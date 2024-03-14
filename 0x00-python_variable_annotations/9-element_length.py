#!/usr/bin/env python3

"""
Implementation of Static typing of Python
"""
from typing import Sequence, Tuple


def element_length(lst: Sequence[str]) -> Sequence[Tuple[str, int]]:
    """Return a sequence of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]