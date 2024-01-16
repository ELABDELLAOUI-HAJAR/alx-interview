#!/usr/bin/python3

"""
  This script contains the implementation of
  minOperations function
"""


def minOperations(n):
    """function that return the minimum operations needed
    to print n"H" in a file by using two operations "Copy All"
    and "Paste"
    """
    nbr_operation = 0
    min_divisor = 2

    while n > 1:
        while n % min_divisor == 0:
            nbr_operation += min_divisor
            n /= min_divisor
        min_divisor += 1
    return nbr_operation
