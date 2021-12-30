import numpy as np

from src.functions import read_input


def main():
    positions = np.array(list(map(int, read_input(7)[0].split(','))))
    cheaper_cost = _get_cheaper_cost(positions, True)
    print(f'Cheaper cost is {cheaper_cost}')
    cheaper_cost = _get_cheaper_cost(positions, False)
    print(f'Cheaper cost is {cheaper_cost}')


def _get_cheaper_cost(positions, part1):
    max_horizontal = positions.max()
    costs = np.array([None] * max_horizontal)
    for i in range(max_horizontal):
        costs[i] = 0
        for original_position in positions:
            costs[i] += _cost(original_position, i, part1)
    return costs.min()


def _cost(original_position, destination, part1):
    if part1:
        return abs(original_position - destination)
    return np.arange(1, abs(original_position - destination) + 1).sum()


if __name__ == '__main__':
    main()
