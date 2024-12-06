from solver import utils
import sys
import time

def move(pos, direction, map):
    new_y = pos[0] + direction[0]
    new_x = pos[1] + direction[1]
    if not (new_y >= 0 and new_x >= 0):
        return None

    try:
        if map[new_y][new_x] == "#":
            return pos
        else:
            return (new_y, new_x)
    except:
        return None



def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]

    obstacles = set()
    guard = {}
    visited = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((y,x))
            if not char in [".", "#"]:
                guard["pos"] = (y,x)
                guard["facing"] = (-1, 0)
    
    current_pos = guard["pos"]
    current_facing = guard["facing"]

    steps = 0
    new_map  = lines.copy()
    got_out = False
    while not got_out and steps < 10000:
        visited.add(current_pos)
        new_map[current_pos[0]][current_pos[1]] = "X"

        new_pos = move(current_pos, current_facing, lines)

        if new_pos != current_pos and new_pos:
            #print(f"{current_pos}, Next valid, moving: {new_pos} DIR {current_facing}")
            current_pos = new_pos

        elif new_pos == current_pos:
            if current_facing == (-1,0):
                current_facing = (0, 1)
            elif current_facing == (0, 1):
                current_facing = (1, 0)
            elif current_facing == (1, 0):
                current_facing = (0, -1)
            elif current_facing == (0, -1):
                current_facing = (-1, 0)
        else:
            got_out = True
            new_map[current_pos[0]][current_pos[1]] = "O"
            print("HE GOT OUT")
            print(current_pos, new_pos, current_facing)
        
        #print("\033[u", end="")
        #for y in new_map:
        #    print("".join(y))
        #time.sleep(0.001)
        
    #print(len(visited))

    #for y in new_map:
    #        print("".join(y))
    return len(visited)
        



