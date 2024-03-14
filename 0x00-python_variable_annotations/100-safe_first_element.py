#!/usr/bin/env python3

"""
Implementation of Static typing of Python
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe first element function
    """
    if lst:
        return lst[0]
    else:
        return None
