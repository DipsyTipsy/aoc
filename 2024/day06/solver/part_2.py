from solver import utils
from collections import defaultdict
from copy import deepcopy
import time

def step(pos, direction, grid):
    new_y = pos[0] + direction[0]
    new_x = pos[1] + direction[1]
    if new_y in range(len(grid)) and new_x in range(len(grid)):
        return ((new_y, new_x,), grid[new_y][new_x])
    else:
        return (None, None)

def rotate(current_facing):
    if current_facing == (-1,0):
        return (0, 1)
    elif current_facing == (0, 1):
        return (1, 0)
    elif current_facing == (1, 0):
        return (0, -1)
    elif current_facing == (0, -1):
        return (-1, 0)

def check_loop(start, facing, grid):
    _visited = set()
    _pos = start
    _facing = facing
    print("\t- Starting check from", _pos)

    _step = 0

    while True:
        if (_pos, _facing) in _visited:
        # if this works i go to bed
        #if _step > 10000:
            print("\t- Loop", _pos, _facing)
            return True
        
        _visited.add((_pos, _facing))
        new_pos, item = step(_pos, _facing, grid)

        if item in [".", "^"]:
        #    print("\t\tWalk")
            _pos = new_pos
        elif item == "#":
        #    print("\t\tTurn")
            _facing = rotate(_facing)
        else:
            print("\t- Got Out, Not Loop", _pos)
            return False
        _step += 1

def solve(input_file: str):
    print("PART 2")
    print()
    lines = [[y for y in x] for x in utils.read_lines(input_file)]

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char in [".", "#"]:
                current_pos = (y,x)
                current_facing = (-1, 0)
    
    print("Starting from", current_pos)
    new_map  = [x.copy() for x in lines.copy()]
    block_map = [x.copy() for x in lines.copy()]
    possible_blocker = set()
    visited = set()

    while True:
        # Check if possible blocker
        blocker, b_c = step(current_pos, current_facing, lines)
        if not blocker in possible_blocker and b_c == ".":
            print("Check from ", (current_pos, current_facing), "Possible Blocker", blocker, b_c)
            lines[blocker[0]][blocker[1]] = "#"

            if check_loop(current_pos, current_facing, lines):
                possible_blocker.add(blocker)
                block_map[blocker[0]][blocker[1]] = "O"
            
            lines[blocker[0]][blocker[1]] = "."

        visited.add((current_pos))
        new_map[current_pos[0]][current_pos[1]] = "X"

        new_pos, item = step(current_pos, current_facing, lines)
        if item in [".", "^"]:
            current_pos = new_pos
        elif item == "#":
            current_facing = rotate(current_facing)
        else:
            new_map[current_pos[0]][current_pos[1]] = "O"
            break

        
        
    print()
    for y in block_map:
        print("".join(y))
    
    print(len(visited), len(possible_blocker))
    return len(possible_blocker)