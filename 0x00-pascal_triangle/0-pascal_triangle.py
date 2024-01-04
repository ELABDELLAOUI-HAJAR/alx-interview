#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """Definition of pascal_triangle function
      args: n the length od the triangle
      Returns a list of lists of integers representing
      the Pascal’s triangle
    """

    if n <= 0:
        return []

    pascal_triangle = [[1]]
    while len(pascal_triangle) != n:
        last_elmt = pascal_triangle[-1]
        next_elmt = [1]
        for i in range(0, len(last_elmt) - 1):
            next_elmt.append(last_elmt[i] + last_elmt[i + 1])
        next_elmt.append(1)
        pascal_triangle.append(next_elmt)
    return pascal_triangle
