from solver import utils
import re



def solve(input_file: str):
    lines = utils.read_lines(input_file)

    max_y = len(lines)
    max_x = len(lines[0])
    symbols = [[False for i in range(max_x)] for j in range(max_y)]

    def set_location(y, x):
        if(x >= 0 and y >= 0  and x <= max_x and y <= max_y):
            symbols[y][x] = True

    for i, line in enumerate(lines):
        for m in re.finditer(r"([^\d\.])", line):
            set_location(i, m.start(0)-1)
            set_location(i-1, m.start(0)-1)
            set_location(i-1, m.start(0))
            set_location(i-1, m.start(0)+1)
            set_location(i, m.start(0)+1)
            set_location(i+1, m.start(0)+1)
            set_location(i+1, m.start(0))
            set_location(i+1, m.start(0)-1)

    numbers = []
    for i, line in enumerate(lines):
        for m in re.finditer(r"(\d+)", line):
            if any([symbols[i][j] for j in range(m.start(0), m.end(0))]):
                numbers.append(int(m.group()))




    return sum(numbers)
