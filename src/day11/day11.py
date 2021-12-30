import numpy as np

from src.functions import read_input


def main():
    grid = np.array(list(map(lambda x: [int(y) for y in list(x)], read_input(11))))

    flashes = 0
    for i in range(100):
        grid, new_flashes = _run_step(grid)
        flashes += new_flashes
    print(f'Total flashes: {flashes}')

    grid = np.array(list(map(lambda x: [int(y) for y in list(x)], read_input(11))))
    step_count = 0
    while grid.sum() != 0:
        grid, _ = _run_step(grid)
        step_count += 1
    print(f'All flashing in step: {step_count}')


def _run_step(grid):
    flashes = 0
    grid += 1
    flashed = []
    to_flash = np.argwhere(grid > 9)
    while len(to_flash):
        i, j = to_flash[-1]
        to_flash = to_flash[:-1]
        flashes += 1
        flashed.append([i, j])
        for coordinates in [
            (i-1, j-1),  # noqa: E226
            (i-1, j),  # noqa: E226
            (i-1, j+1),  # noqa: E226
            (i, j-1),  # noqa: E226
            (i, j+1),  # noqa: E226
            (i+1, j-1),  # noqa: E226
            (i+1, j),  # noqa: E226
            (i+1, j+1),  # noqa: E226
        ]:
            grid, to_flash = _check_coordinate(grid, coordinates[0], coordinates[1], flashed, to_flash)

    grid = grid * (grid <= 9)
    return grid, flashes


def _check_coordinate(grid, i, j, flashed, to_flash):
    if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
        if grid[i][j] <= 9:
            grid[i][j] += 1
            if grid[i][j] > 9 and [i, j] not in flashed and [i, j] not in to_flash.tolist():
                to_flash = np.vstack([to_flash, [i, j]])
    return grid, to_flash


if __name__ == '__main__':
    main()
