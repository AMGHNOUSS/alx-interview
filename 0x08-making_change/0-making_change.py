#!/usr/bin/python3
""" Making Change"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1
        if total == 0:
            return coin_count
    return -1
