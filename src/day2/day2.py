from functools import reduce


def main():
    with open('day2.txt', mode='r') as open_file:
        input_data = list(map(lambda x: x.strip(), open_file.readlines()))
    parsed_commands = list(map(_parse_commands, input_data))

    final_position = (list(map(sum, zip(*parsed_commands))))
    print(f'Answer for part 1 is: {final_position[0] * final_position[1]}')

    final_measurements = reduce(_compute_position_part_2, parsed_commands, {'aim': 0, 'depth': 0, 'horizontal': 0})
    print(f'Answer for part 2 is: {final_measurements["horizontal"] * final_measurements["depth"]}')


def _parse_commands(command):
    if 'forward' in command:
        return [int(command.split()[1]), 0]
    elif 'down' in command:
        return [0, int(command.split()[1])]
    else:
        return [0, -int(command.split()[1])]


def _compute_position_part_2(acc, command):
    return {
        'aim': acc['aim'] + command[1],
        'depth': acc['depth'] + acc['aim'] * command[0],
        'horizontal': acc['horizontal'] + command[0]
    }


if __name__ == '__main__':
    main()
