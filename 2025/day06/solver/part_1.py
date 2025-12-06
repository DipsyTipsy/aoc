from solver import utils
import re


def solve(input_file: str):
    lines = [re.sub(r"\s+", "," ,x.strip()).split(",") for x in utils.read_lines(input_file)]

    operations = lines[-1]
    problems = [0] * len(lines[-1])
    for i, op in enumerate(operations):
        if op == "*":
            problems[i] = 1

    for line in lines[:-1]:
        for i in range(len(line)):
           match operations[i]:
                case "*":
                   problems[i] *= int(line[i])
                case "+":
                   problems[i] += int(line[i])


    return sum(problems)

