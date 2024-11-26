#!/usr/bin/python3
""" Making Change"""


def makeChange(coins, total):
    if (total < 1 ):
        return 0
    coins = sorted(coins, reverse=True)
    l = len(coins)
    index = 0
    i = 0
    while (total != 0 and i < l):
        if (total > coins[i]):
            total = total - coins[i]
            index = index + 1
        else:
            i = i + 1
        if (total < coins[l - 1]):
            index = 0
    if (index == 0):
        return -1
    return index