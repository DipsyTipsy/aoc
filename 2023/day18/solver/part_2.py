from solver import utils
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import math
import re

def solve(input_file: str):
    lines = [tuple(x.split()) for x in utils.read_lines(input_file)]
    print("Part 2")

    directions = {
        "U": (-1,0),
        "D": (1,0),
        "R": (0,1),
        "L": (0,-1),
                  }
    dir_short = ["R", "D", "L", "U"]


    current_node = (0,0)
    nodes = [current_node]
    for line in lines:
        dir, length, color = line
        print(dir,length,color)

        instruction = re.sub(r"[#\(\)]", "", color)
        dir, length = dir_short[int(instruction[-1])], int(instruction[:-1], 16)

        current_node = (current_node[0] + directions[dir][0]*int(length), current_node[1] + directions[dir][1]*int(length))
        nodes.append(current_node)
    
    
    dig_plan = Polygon(nodes)
    print(dig_plan.area, int(dig_plan.exterior.length), dig_plan)

    plt.plot(*dig_plan.exterior.xy)
    plt.savefig("dig_plan.png")

    lava_area = int(dig_plan.area) - int(dig_plan.exterior.length)*0.5 + dig_plan.exterior.length + 1


    return lava_area