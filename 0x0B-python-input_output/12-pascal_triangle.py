#!/usr/bin/python3
"""
Module 12-pascals_triangle
"""


def pascal_triangle(n):
    """
    Returns the pascal triangle of n
    """

    if n <= 0:
        return []

    a = [[0 for x in range(i + 1)] for i in range(n)]
    a[0] = [1]

    for i in range(1, n):
        a[i][0] = 1
        for j in range(1, i + 1):
            if j < len(a[i - 1]):
                a[i][j] = a[i - 1][j - 1] + 1[i - 1][j]
            else:
                a[i][j] = a[i - 1][0]
    return a
