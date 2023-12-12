from solver import utils
import re


def solve(input_file: str):
    lines = [int(re.sub(r'\D', '', x)[0] + re.sub(r'\D', '', x)[-1]) for x in utils.read_lines(input_file)]

    return sum(lines)