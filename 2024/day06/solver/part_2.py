from solver import utils
from collections import defaultdict
import time

def step(pos, direction, map):
    new_y = pos[0] + direction[0]
    new_x = pos[1] + direction[1]
    if new_y >= 0 and new_x >= 0 and new_y < len(map) and new_x < len(map):
        return ((new_y, new_x,), map[new_y][new_x])
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

def check_loop(start, facing, map):
    _visited = set()
    _pos = start
    _facing = facing
    #print("\t- Starting check from", _pos, _steps)

    while True:
        if (_pos, _facing) in _visited:
            return True

        _visited.add((_pos, _facing))
        new_pos, item = step(_pos, _facing, map)

        if item not in [None, "#"]:
        #    print("\t\tWalk")
            _pos = new_pos
        elif item == "#":
        #    print("\t\tTurn")
            _facing = rotate(_facing)
        else:
            #print("- Got Out, Not Loop", _pos,  _steps)
            return False

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
        if str((current_pos, current_facing)) in visited:
            break

        blocker, b_c = step(current_pos, current_facing, lines)
        if not blocker in possible_blocker and b_c not in  ["#", "^", None]:
            _lines  = [x.copy() for x in lines.copy()]
            print("Check from ", (current_pos, current_facing), "Possible Blocker", blocker, b_c)
            _lines[blocker[0]][blocker[1]] = "#"

            if check_loop(current_pos, current_facing, _lines):
                possible_blocker.add(str(blocker))
                block_map[blocker[0]][blocker[1]] = "O"
                

        visited.add(str((current_pos, current_facing)))
        new_map[current_pos[0]][current_pos[1]] = "X"

        new_pos, item = step(current_pos, current_facing, lines)
        if item not in [None, "#"]:
            current_pos = new_pos
        elif item == "#":
            current_facing = rotate(current_facing)
        else:
            new_map[current_pos[0]][current_pos[1]] = "O"
            break
        
    print()
    for y in block_map:
        print("".join(y))
    
    return len(possible_blocker)