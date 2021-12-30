from operator import mul
from functools import reduce

from src.functions import read_input


def main():
    grid = list(map(lambda x: [int(y) for y in list(x)], read_input(9)))
    padded_grid = _pad(grid)
    low_points = _get_low_points(padded_grid)

    risk_levels_sum = 0
    for low_point in low_points:
        risk_levels_sum += 1 + grid[low_point[0]-1][low_point[1]-1]  # noqa: E226
    print(f'Risk levels sum: {risk_levels_sum}')

    basin_sizes = _get_basin_sizes(padded_grid, low_points)
    print(f'Sizes of three largest basins multiplied: {reduce(mul, sorted(basin_sizes)[-3:], 1)}')


def _pad(grid):
    '''
    To make it a little easier to traverse the grid without having to care about trying to access indexes out of range.
    '''
    grid = [[9] * len(grid[0])] + grid + [[9] * len(grid[0])]
    grid = [[9] + line + [9] for line in grid]
    return grid


def _get_low_points(padded_grid):
    '''
    Returns coordinates in reference to the padded_grid, not the original grid!
    '''
    low_points = []
    for i, line in enumerate(padded_grid):
        for j, height in enumerate(line):
            if height != 9:
                min_adjacent_height = min(
                    padded_grid[i-1][j],  # noqa: E226
                    padded_grid[i+1][j],  # noqa: E226
                    padded_grid[i][j-1],  # noqa: E226
                    padded_grid[i][j+1],  # noqa: E226
                )
                if height < min_adjacent_height:
                    low_points.append((i, j))
    return low_points


def _get_basin_sizes(padded_grid, low_points):
    basin_sizes = []
    for low_point in low_points:
        to_visit = [low_point]
        visited = []
        size = 1
        while to_visit:
            i, j = to_visit.pop()
            visited.append((i, j))
            for coordinates in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:  # noqa: E226
                to_visit, size = _check_coordinate(padded_grid, coordinates[0], coordinates[1], visited, to_visit, size)

        basin_sizes.append(size)
    return basin_sizes


def _check_coordinate(padded_grid, i, j, visited, to_visit, size):
    if padded_grid[i][j] != 9 and (i, j) not in visited and (i, j) not in to_visit:
        to_visit.append((i, j))
        size += 1
    return to_visit, size


if __name__ == '__main__':
    main()
