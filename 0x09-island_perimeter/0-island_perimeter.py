#!/usr/bin/python3
"""
 This module returns the perimeter of the
 Island described in grid
"""


def island_perimeter(grid):
    """function that returns the perimeter of the island"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check the cell above
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the cell below
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the cell to the left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter

# def island_perimeter(grid):
#     """function that returns the perimeter of the island"""
#     perimeter = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             # If the current cell is land(1)
#             if grid[i][j] == 1:
#                 # Add 4 to the perimeter
#                 perimeter += 4
#                 # If the cell to the left is land(1), subtract 2
#                 if i > 0 and grid[i - 1][j] == 1:
#                     perimeter -= 2
#                 # If the cell above is land, subtract 2
#                 if j > 0 and grid[i][j - 1] == 1:
#                     perimeter -= 2
#     return perimeter
