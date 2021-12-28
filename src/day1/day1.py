def main():
    with open('day1.txt', mode='r') as open_file:
        input_data = list(map(lambda x: int(x.strip()), open_file.readlines()))
    print(f'Direct increases: {_compute_increases(input_data)}')
    rolling_window_data = list(
        map(
            sum, zip(input_data[:-2], input_data[1:-1], input_data[2:])
        )
    )
    print(f'Rolling window increases: {_compute_increases(rolling_window_data)}')


def _compute_increases(input_array):
    return sum(
        map(
            lambda data: data[0] < data[1],
            zip(input_array[:-1], input_array[1:])
        )
    )


if __name__ == '__main__':
    main()
