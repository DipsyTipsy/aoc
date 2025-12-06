from solver import utils
import re, math
from collections import defaultdict

def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]
    problems = defaultdict(str)
    for line in lines:
        for i, x in enumerate(line):
            problems[i] +=x

    parsed_problems = defaultdict(list)
    operations = {}
    idx = 0
    for i, problem in problems.items():
        if all((x == " " for x in problem)):
            idx+=1
            continue
        if "*" in problem:
            operations[idx] = "*"
            problem = problem.replace("*", "")
        elif "+" in problem:
            operations[idx] = "+"
            problem = problem.replace("+", "")
        parsed_problems[idx].append(problem.strip())

    totals = []
    for i, op in operations.items():
        num = parsed_problems[i]
        match op:
            case "*":
                totals.append(math.prod((int(x) for x in num)))
            case "+":
                totals.append(sum(int(x) for x in num))
    return sum(totals)