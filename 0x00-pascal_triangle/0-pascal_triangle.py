#!/usr/bin/python3
""" Create Pascale Triangle"""


def pascal_triangle(n):
    if (n <= 0):
        return None
    else:
        res = []
        for i in range(1, n + 1):
            item = []
            C = 1
            for j in range(1, i + 1):
                item.append(C)
                C = C * (i - j) // j
            res.append(item)
    return res
