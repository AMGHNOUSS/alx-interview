#!/usr/bin/python3
""" Rotate 2D matrix."""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    matrix_change = [[matrix[i % n][j % n] for j in range(n)]
                     for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = matrix_change[n - 1 - j][i]
