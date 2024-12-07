
from solver import utils

rotate = {
    (-1,  0): (0, 1),
    ( 0,  1): (1, 0),
    ( 1,  0): (0, -1),
    ( 0, -1): (-1, 0),
}

def get_pos(pos, grid):
    if all([cord in range(len(grid)) for cord in pos]):
        return grid[pos[0]][pos[1]]
    else:
        return None

def step(pos, facing, grid):
    n_pos = (pos[0]+facing[0], pos[1] + facing[1])

    val = get_pos(n_pos, grid)
    if val:
        return n_pos, val
    else:
        return None, None

def move(pos, facing, grid):
    next_pos, next_val = step(pos, facing, grid)
    next_facing = facing
    match next_val:
        case ".":
            current_pos = next_pos
            next_facing = facing
        case "#":
            next_pos = pos
            next_facing = rotate[facing]
        case None:
            next_pos = None
            next_facing = None

    return next_pos, next_facing

def solve(input_file: str):
    print("PART 2")
    print()
    lines = [[y for y in x] for x in utils.read_lines(input_file)]

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                current_pos = (y,x)
                current_facing = (-1, 0)
    
    start_pos = current_pos
    start_facing = current_facing
    print("Starting from", current_pos, current_facing)

    visited = set()
    blockers = set()
    while current_pos:
        if current_pos:
            visited.add(current_pos)
            #print(current_pos, current_facing)

        current_pos, current_facing = move(current_pos, current_facing, lines)
    
    for pos in visited:
        if pos not in blockers:
            lines[pos[0]][pos[1]] = "#"
            print("- Checking blocker", pos)
            simulated_pos, simulated_facing = start_pos, start_facing

            simulated_visited = set()
            while simulated_pos and not (simulated_pos, simulated_facing) in simulated_visited:

                if simulated_pos:
                    simulated_visited.add((simulated_pos, simulated_facing))

                simulated_pos, simulated_facing = move(simulated_pos, simulated_facing, lines)

            if (simulated_pos, simulated_facing) in simulated_visited and simulated_pos:
                blockers.add(pos)

            lines[pos[0]][pos[1]] = "."


    print(len(blockers))
    print(len(visited))
    return len(blockers)