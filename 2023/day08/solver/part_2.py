from solver import utils
import re
import numpy as np
import math


def solve(input_file: str):
    print()
    lines = utils.read_lines(input_file)

    instructions = list(lines[0])
    paths = {}
    for line in lines[2:]:
        current_line = re.sub(r'[\=\(\),]', '', line).split()
        paths[current_line[0]] = {"L": current_line[1], "R": current_line[2]}

    positions = {}
    for path in paths:
        if path[2] == "A":
            positions[path] = path

    def all_at_goal(positions):
        return all(position[2] == "Z" for position in positions.values())
    
    steps = 0
    goals = {key: {}  for key in positions.keys()}
    while not all_at_goal(positions):
        for key, position in positions.items():
            options = paths[position]
            dest = options[instructions[steps % len(instructions)]]
            if (position[2] == "Z"):
                if position in goals[key]:
                    goals[key][position].append(steps)
                else:
                    goals[key][position] = [0,steps]

            positions[key] = dest

        steps += 1
        if steps > 100000:
            break

    increments = []
    for goal, step in goals.items():
        increment = [y-x for x, y in utils.sliding_window(list(step.values())[0], 2, 1)]
        if increment:
            increments.append(max(increment))

    # Find the least common demoniator in order to find where all loops meet
    prod = math.lcm(*increments)

    positions = []
    for line in increments:
         value = line + (line * prod) 
         positions.append(value%line)        

    print(positions)
  
    return prod