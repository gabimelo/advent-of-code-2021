import os


def read_input(day):
    with open(f'src/day{day}/day{day}.txt', mode='r') as open_file:
        return list(map(lambda x: x.strip(), open_file.readlines()))
