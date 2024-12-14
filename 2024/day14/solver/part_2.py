from solver import utils
from collections import defaultdict
import re
import time


def solve(input_file: str, grid_y, grid_x):
    lines = [[[int(z) for z in y.split(",")] for y in re.findall(r"(-?\d+,-?\d+)", x)] for x in utils.read_lines(input_file)]

    time_range = 1000000
    

    for t in range(time_range):
        print(t)
        robots = defaultdict(int)
        grid = [ ["."]*grid_x for y in range(grid_y)]
        for line in lines:
            y = line[0][1]
            x = line[0][0]

            dy = line[1][1]
            dx = line[1][0]

            end_y = (y + t*dy) % grid_y
            end_x = (x + t*dx) % grid_x
            robots[(end_x, end_y)] +=1

        if all( [x == 1 for x in robots.values()]):
            print("found it")
        
            for pos, num in robots.items():
                grid[pos[1]][pos[0]] = num
            for line in grid:
                print(line)
            break
