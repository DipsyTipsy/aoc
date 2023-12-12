from solver import utils
import re


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    start = "AAA"
    goal = "ZZZ"

    instructions = list(lines[0])
    paths = {}
    for line in lines[2:]:
        current_line = re.sub(r'[\=\(\),]', '', line).split()
        paths[current_line[0]] = {"L": current_line[1], "R": current_line[2]}

    current = start
    steps = 0
    while not current == goal:
        options = paths[current]
        dest = options[instructions[steps % len(instructions)]]

        current = dest

        steps += 1


    return steps