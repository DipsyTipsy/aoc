import sympy.core
import sympy.core.numbers
from solver import utils
import numpy as np
import re
import sympy
from sympy.abc import c,d


def solve(input_file: str):
    lines = "|".join(utils.read_lines(input_file))


    lines = lines.split("||")

    total_tokens = 0
    for task in lines:
        cur_task = task.split("|")
        a = np.array([int(x) for x in re.findall(r"\+(\d+)", cur_task[0])])
        b = np.array([int(x) for x in re.findall(r"\+(\d+)", cur_task[1])])
        prize = np.array([int(x)+10000000000000 for x in re.findall(r"\=(\d+)", cur_task[2])])

        tokens_spent = [] 

        e1 = (c*a[0] + d*b[0]) - prize[0]
        e2 = (c*a[1] + d*b[1]) - prize[1]

        solution = sympy.solve([e1, e2])

        if type(solution[c]) == sympy.core.numbers.Integer:
            print("Winner", "A: ", solution[c], "B: ", solution[d])
            tokens_spent.append((solution[c])*3+(solution[d])*1)
        else:
            print("No Winner")

        if len(tokens_spent) > 0:
            total_tokens += min(tokens_spent)

    print("Total", total_tokens)
    return total_tokens
        




