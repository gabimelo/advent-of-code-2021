from functools import reduce
from operator import iconcat

from src.functions import read_input


def main():
    input_data = read_input(8)
    print(f'''All-functional part 1 just for fun: {
        sum(
            map(
                lambda x: len(x) < 5 or len(x) == 7,
                reduce(
                    iconcat,
                    map(
                        lambda x: x.split(" | ")[1].split(),
                        input_data
                    ),
                    []
                )
            )
        )
    }''')

    output_digits_sum = 0
    for puzzle in input_data:
        puzzle_pieces = puzzle.split(' | ')
        puzzle_wires = list(map(lambda x: ''.join(sorted(x)), puzzle_pieces[0].split()))
        puzzle_outputs = puzzle_pieces[1].split()
        digits = {}
        for wires in puzzle_wires:
            length = len(wires)
            if length == 2:
                digits[1] = wires
            elif length == 3:
                digits[7] = wires
            elif length == 4:
                digits[4] = wires
            elif length == 7:
                digits[8] = wires
            elif length == 5:
                if 1 not in digits:
                    puzzle_wires.append(wires)
                else:
                    if all(wire in wires for wire in digits[1]):
                        digits[3] = wires
                    else:
                        if 4 not in digits:
                            puzzle_wires.append(wires)
                        else:
                            if sum(wire in wires for wire in digits[4]) == 3:
                                digits[5] = wires
                            else:
                                digits[2] = wires
            elif length == 6:
                if 1 not in digits:
                    puzzle_wires.append(wires)
                else:
                    if not all(wire in wires for wire in digits[1]):
                        digits[6] = wires
                    else:
                        if 4 not in digits:
                            puzzle_wires.append(wires)
                        else:
                            if all(wire in wires for wire in digits[4]):
                                digits[9] = wires
                            else:
                                digits[0] = wires

        output_digits = ''
        for output in puzzle_outputs:
            output_digits += str(list(digits.keys())[list(digits.values()).index(''.join(sorted(output)))])
        output_digits_sum += int(output_digits)

    print(f'Part 2: {output_digits_sum}')


if __name__ == '__main__':
    main()
