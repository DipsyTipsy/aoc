from solver import utils
from functools import reduce
from operator import mul
import re



def solve(input_file: str):
    lines = utils.read_lines(input_file)

    max_y = len(lines)
    max_x = len(lines[0])
    possible_gear_loc = {}
    gears = []
    numbers = [{} for j in range(max_y)]

    def possible_loc(symbol_loc, y, x):
        if(x >= 0 and y >= 0  and x <= max_x and y <= max_y):
            possible_gear_loc[symbol_loc].append((y,x))

    for i, line in enumerate(lines):
        for m in re.finditer(r"([\*])", line):
            possible_gear_loc[(i, m.start(0))] = []
            possible_loc((i, m.start(0)), i, m.start(0)-1)
            possible_loc((i, m.start(0)), i-1, m.start(0)-1)
            possible_loc((i, m.start(0)), i-1, m.start(0))
            possible_loc((i, m.start(0)), i-1, m.start(0)+1)
            possible_loc((i, m.start(0)), i, m.start(0)+1)
            possible_loc((i, m.start(0)), i+1, m.start(0)+1)
            possible_loc((i, m.start(0)), i+1, m.start(0))
            possible_loc((i, m.start(0)), i+1, m.start(0)-1)

    for i, line in enumerate(lines):
        for m in re.finditer(r"(\d+)", line):
            value = m.group()
            x = range(m.start(0), m.end(0))
            key = hash(f"{value}.{x}")
            numbers[i][key] = (value, x)

    for gear, locations in possible_gear_loc.items():
        adjacent_numbers = set()
        for loc in locations:
            for key, numb in numbers[loc[0]].items():
                if loc[1] in numb[1]: 
                    adjacent_numbers.add(numb)
        if len(adjacent_numbers) == 2:
            gears.append(reduce(mul, [int(x[0]) for x in adjacent_numbers]))

    return sum(gears)


