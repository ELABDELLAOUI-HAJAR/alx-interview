#!/usr/bin/python3
"""0-island_perimeter Module contains island_perimeter function"""


def cell_nbr_water(grid, row, col):
    """returns the number of water surround a cell"""
    water_num = 0

    if row <= 0 or not grid[row - 1][col]:
        water_num += 1
    if row >= len(grid) - 1 or not grid[row + 1][col]:
        water_num += 1
    if col <= 0 or not grid[row][col - 1]:
        water_num += 1
    if col >= len(grid[row]) - 1 or not grid[row][col + 1]:
        water_num += 1

    return water_num


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                perimeter += cell_nbr_water(grid, row, col)

    return perimeter
