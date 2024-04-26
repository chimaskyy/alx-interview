#!/usr/bin/python3

"""This module contains paschal triangle function
    ALGORITHM:
    1. create a triangle list of 1's
    2. iterate through the triangle list, skipping the first two rows
    3. iterate through each row, starting from the second element
    to the second last element
    4. set the current element to the sum of the element
    above and the element above to the left
    5. return the triangle list
"""


def pascal_triangle(n):
    """This function returns a list of lists
    of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    # create a triangle list of 1's
    triangle = [[1] * i for i in range(1, n + 1)]

    # iterate through the triangle list, skipping the first two rows
    for i, row in enumerate(triangle):
        if i < 2:
            continue
        # iterate through each row, starting from the second element
        for j in range(1, len(row) - 1):
            # set the current element to the sum of the element above
            # and the element above to the left
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
