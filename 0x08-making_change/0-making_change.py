#!/usr/bin/python3
"""Making changes module"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a
    given amount total by given a pile of coins of
    different values
    """

    if total <= 0:
        return 0

    coins_count = 0
    reste = total
    idx = 0
    sorted_list_coins = sorted(coins, reverse=True)
    n = len(coins)
    while reste > 0:
        if idx >= n:
            return -1
        if reste - sorted_list_coins[idx] >= 0:
            reste -= sorted_list_coins[idx]
            coins_count += 1
        else:
            idx += 1
    return coins_count
