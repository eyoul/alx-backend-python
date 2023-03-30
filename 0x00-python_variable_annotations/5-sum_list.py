#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum a list of floats
    Args:
        input_list (list): A list of floats
    Returns:
        float: the sum of the float in the list
    """
    if input_list in None:
        return 0
    else:
        return sum(input_list)
