#!/usr/bin/python3
"""This module rotates a 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise"""
    matrix[:] = [list(i) for i in zip(*matrix)]
    for row in matrix:
        row.reverse()
