from solver import utils
from collections import defaultdict


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    left_list = defaultdict(int)
    right_list = defaultdict(int)

    for line in lines:
        data  = [int(x) for x in line.split("  ")]

        left_list[data[0]] += 1
        right_list[data[1]] += 1


    scores = []
    for item, count in left_list.items():
        scores.append(count * item * right_list.get(item, 0))

    return sum(scores)