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
        a = [int(x) for x in re.findall(r"\+(\d+)", cur_task[0])]
        b = [int(x) for x in re.findall(r"\+(\d+)", cur_task[1])]
        prize = np.array([int(x) for x in re.findall(r"\=(\d+)", cur_task[2])])

        tokens_spent = [] 
        y = np.arange(0,100) 
        x = (prize[0] - y*b[0])/a[0]

        possible_y = np.where(np.equal(np.mod(x, 1), 0))[0]
        for y in possible_y:
            py = a[1]*x[y] + y*b[1]
            if py == prize[1]:
                tokens_spent.append((x[y])*3+(y)*1)

        tokens_spent = [] 

        e1 = (c*a[0] + d*b[0]) - prize[0]
        e2 = (c*a[1] + d*b[1]) - prize[1]

        solution = sympy.solve([e1, e2])

        if type(solution[c]) == sympy.core.numbers.Integer:
            print("Winner", solution[c], solution[d])
            tokens_spent.append((solution[c])*3+(solution[d])*1)


        if len(tokens_spent) > 0:
            total_tokens += min(tokens_spent)

    print(total_tokens)
    return total_tokens