from statistics import median

from src.functions import read_input


def main():
    lines = read_input(10)
    stack = []
    illegals = []
    scores = []

    for line in lines:
        corrupted = False
        for char in line:
            if char in opening_pairs.values():
                stack.append(char)
            else:
                if stack[-1] == opening_pairs[char]:
                    stack.pop()
                else:
                    illegals.append(char)
                    corrupted = True
                    stack = []
                    break
        if not corrupted:
            score = 0
            while stack:
                next_to_close = stack.pop()
                score = score * 5 + completion_points[next_to_close]
            scores.append(score)

    print(f'Illegals: {illegals}. Total points: {sum(map(lambda x: points[x], illegals))}')
    print(f'Middle score: {median(scores)}')


opening_pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


completion_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


if __name__ == '__main__':
    main()
