#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    matrix[:] = [list(i) for i in zip(*matrix)]
    for row in matrix:
        row.reverse()
    return matrix
