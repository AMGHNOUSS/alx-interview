#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    line = len(grid)
    row = len(grid[0])
    sum = 0
    check = 0

    for i in range(line):
        for j in range(row):
            check = 0
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
    return (sum)
