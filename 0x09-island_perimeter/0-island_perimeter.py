#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island."""
    line = len(grid)
    row = len(grid[0])
    sum = 0
    check = 0

    for i in range(line):
        for j in range(row):
            if (grid[i][j] == 1):
                if (j < row and grid[i][j + 1] == 0):
                    check += 1
                if (j > -1 and grid[i][j - 1] == 0):
                    check += 1
                if (i < line and grid[i + 1][j] == 0):
                    check += 1
                if (i > -1 and grid[i - 1][j] == 0):
                    check += 1
                sum += check
                check = 0
    return (sum)
