from solver import utils
from collections import defaultdict
import re


def solve(input_file: str, grid_y, grid_x):
    lines = [[[int(z) for z in y.split(",")] for y in re.findall(r"(-?\d+,-?\d+)", x)] for x in utils.read_lines(input_file)]

    print(lines)
    time = 100
    robots = defaultdict(int)

    
    for line in lines:
        y = line[0][1]
        x = line[0][0]

        dy = line[1][1]
        dx = line[1][0]

        print("y,x", (y,x),"velocity", (dy,dx))
        end_y = (y + time*dy) % grid_y
        end_x = (x + time*dx) % grid_x
        print("Ends up at", (end_x, end_y))
        robots[(end_x, end_y)] +=1
    

    quandrants = [0,0,0,0]
    half_y = int(grid_y/2)
    half_x = int(grid_x/2)
    for pos, num in robots.items():
        if pos[0] < half_x and pos[1] < half_y:
            quandrants[0] += num
            quad = 0
        elif pos[0] > half_x and pos[1] < half_y:
            quandrants[1] += num
            quad = 1
        elif pos[0] < half_x and pos[1] > half_y:
            quandrants[2] += num
            quad = 2
        elif pos[0] > half_x and pos[1] > half_y:
            quandrants[3] += num
            quad = 3
        print(pos, num, quad)


    total = 1
    for i in range(len(quandrants)):
        total = quandrants[i]*total
    print(total)
    return total
