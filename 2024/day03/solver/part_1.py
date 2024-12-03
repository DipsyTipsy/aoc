from solver import utils
import re


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print()

    data = re.findall(r"mul\(\d+,\d+\)", str(lines))

    total = 0
    for d in data:
        x, y  = d.replace("mul(", "").replace(")", "").split(",")
        total += int(x)*int(y)

    return total

