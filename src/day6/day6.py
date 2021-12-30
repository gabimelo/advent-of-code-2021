import numpy as np

from src.functions import read_input


def main():
    fish = np.array(list(map(int, read_input(6)[0].split(','))))
    amount = _get_amount_of_fish(fish, rounds=80)
    optimized_amount = _get_optimized_amount_of_fish(fish, rounds=80)
    assert amount == optimized_amount
    print(f'Final amount of fish is {amount}')
    amount = _get_optimized_amount_of_fish(fish, rounds=256)
    print(f'Final amount of fish is {amount}')


def _get_amount_of_fish(fish, rounds):
    fish = fish.copy()
    for i in range(rounds):
        fish = fish - 1
        num_minus_one = (fish == -1).sum()
        fish = np.append(fish, [8] * num_minus_one)
        fish = fish + (fish == -1) * 7
    return len(fish)


def _get_optimized_amount_of_fish(fish, rounds):
    initial_counts = np.unique(fish, return_counts=True)
    amount_at_each_day = [0] * 9
    for index, amount in zip(*initial_counts):
        amount_at_each_day[index] = amount
    for i in range(rounds):
        amount_at_each_day = np.roll(amount_at_each_day, -1)
        amount_at_each_day[6] += amount_at_each_day[8]
    return amount_at_each_day.sum()


if __name__ == '__main__':
    main()
