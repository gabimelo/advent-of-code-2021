import numpy as np

from src.functions import read_input


def main():
    input_data = read_input(5)
    lines = _parse_lines(input_data)
    unidimensional_lines = _get_unidimensional_lines(lines)
    mapped_lines = _get_map(unidimensional_lines)
    print(f'The number of dangerous points is {np.sum(mapped_lines > 1)}')
    mapped_lines = _get_map(lines)
    print(f'The number of dangerous points is {np.sum(mapped_lines > 1)}')


def _parse_lines(input_data):
    parsed_lines = []
    for line in input_data:
        parsed_line = []
        coordinate_pairs = line.split(' -> ')
        for coordinates in coordinate_pairs:
            coordinate_pieces = coordinates.split(',')
            parsed_line.append([int(coordinate_pieces[0]), int(coordinate_pieces[1])])
        parsed_lines.append(parsed_line)
    return parsed_lines


def _get_unidimensional_lines(lines):
    unidimensional_lines = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            unidimensional_lines.append(line)
    return unidimensional_lines


def _get_map(lines):
    max_dimension = np.max(np.array(lines))
    mapped_lines = np.zeros((max_dimension + 1, max_dimension + 1))
    for line in lines:
        x_start = line[0][0]
        x_end = line[1][0]
        y_start = line[0][1]
        y_end = line[1][1]
        distance = max(abs(x_end - x_start), abs(y_end - y_start)) + 1
        x = x_start
        y = y_start
        for i in range(distance):
            mapped_lines[x][y] += 1
            if x < x_end:
                x += 1
            if x > x_end:
                x -= 1
            if y < y_end:
                y += 1
            if y > y_end:
                y -= 1

    return mapped_lines


if __name__ == '__main__':
    main()
