#!/usr/bin/python3
"""Defines prime game function."""


def isWinner(x, nums):

    lenght = len(nums)
    numbers_prime = 0
    index = 0
    for i in range(lenght):
        index = 0
        for j in range(2, nums[i]):
            if (nums[i] % j == 0):
                index += 1
        if (index == 0):
            numbers_prime += 1
    x -= numbers_prime
    if (x <= 0):
        return None
    elif (x % 2 == 0):
        return "Maria"
    else:
        return "Ben"
