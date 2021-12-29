from operator import ge, lt


def main():
    with open('day3.txt', mode='r') as open_file:
        input_data = list(map(lambda x: x.strip(), open_file.readlines()))
    amount_of_ones = _get_amount_of_ones(input_data)
    gamma_rate = int(''.join(['1' if x > (len(input_data) // 2) else '0' for x in amount_of_ones]), 2)
    total_sum = int(''.join(['1' for _ in range(len(amount_of_ones))]), 2)

    print(f'Power_consumption: {gamma_rate * (total_sum - gamma_rate)}')

    ratings = []
    for criteria_op in [ge, lt]:
        numbers_selected_by_bit_criteria = input_data
        tries = 0
        while len(numbers_selected_by_bit_criteria) != 1:
            numbers_selected_by_bit_criteria = _get_rating(numbers_selected_by_bit_criteria, tries, criteria_op)
            tries += 1
        ratings.append(numbers_selected_by_bit_criteria[0])

    print(f'Life support rating: {int(ratings[0], 2) * int(ratings[1], 2)}')


def _get_rating(numbers_selected_by_bit_criteria, tries, operator):
    amount_of_ones = _get_amount_of_ones(numbers_selected_by_bit_criteria, tries)
    to_keep = '1' if operator(amount_of_ones, (len(numbers_selected_by_bit_criteria) / 2)) else '0'
    return list(filter(None, [x if x[tries] == to_keep else None for x in numbers_selected_by_bit_criteria]))


def _get_amount_of_ones(data, position=None):
    full_list = list(map(lambda x: sum([int(item) for item in x]), zip(*data)))
    if position is None:
        return full_list
    return full_list[position]


if __name__ == '__main__':
    main()
