#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    line = len(grid)
    for items in grid:
        row = len(items)
        break
    sum = 0
    check = 0
    for i in range(0, line):
        for j in range(0, row):
            check = 0
            if (grid[i][j] == 1):
                if (grid[i][j + 1] == 0):
                    check += 1
                if (grid[i][j - 1] == 0):
                    check += 1
                if (grid[i + 1][j] == 0):
                    check += 1
                if (grid[i - 1][j] == 0):
                    check += 1
            sum += check
    return (sum)
