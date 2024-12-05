#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island."""
    lines = len(grid)
    rows = len(grid[0])
    sum = 0

    for i in range(lines):
        for j in range(rows):
            if (grid[i][j] == 1):
                if (i == lines - 1 or grid[i + 1][j] == 0):
                    sum += 1
                if (i == 0 or grid[i - 1][j] == 0):
                    sum += 1
                if (j == rows - 1 or grid[i][j + 1] == 0):
                    sum += 1
                if (j == 0 or grid[i][j - 1] == 0):
                    sum += 1
    return (sum)
