import numpy as np

from src.functions import read_input


def main():
    input_data = read_input(4)
    drawn_numbers = list(map(int, input_data[0].split(',')))
    boards = _get_boards(input_data)
    tracker = np.zeros(boards.shape)
    winners = [] 
    while not winners:
        drawn_number = drawn_numbers.pop(0)
        tracker = _play_round(drawn_number, boards, tracker)
        winners = _check_winners(tracker)
    unselected_sum = _get_unselected_sum(winners[0], tracker, boards)
    print(f'Final score is {unselected_sum * drawn_number}')

    winners = []
    while len(winners) < len(boards):
        drawn_number = drawn_numbers.pop(0)
        tracker = _play_round(drawn_number, boards, tracker)
        new_winners = _check_winners(tracker)
        for winner in new_winners:
            if winner not in winners:
                winners.append(winner)
    unselected_sum = _get_unselected_sum(winners[-1], tracker, boards)
    print(f'Final score is {unselected_sum * drawn_number}') 


def _get_boards(input_data):
    boards = []
    board = []
    for line in input_data[1:]:
        if not line:
            if board:
                 boards.append(board)
            board = []
        else:
            board.append(list(map(int, filter(None, line.split(' ')))))
    if board:
         boards.append(board)
    return np.array(boards)
  

def _play_round(drawn_number, boards, tracker):
    tracker += (boards == drawn_number)
    return tracker


def _check_winners(tracker):
    winners = []
    for i, board in enumerate(tracker):
        if 5 in np.sum(board, 0) or 5 in np.sum(board, 1):
            winners.append(i)
    return winners
    

def _get_unselected_sum(winner, tracker, boards):
    return np.sum(((tracker == 0) * boards)[winner])

if __name__ == '__main__':
    main()
