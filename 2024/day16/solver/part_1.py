from solver import utils
from collections import defaultdict

directions = {
    (1,0): [(0,-1), (0, 1), (1,0)],
    (-1,0): [(0,-1), (0,1), (-1,0)],
    (0,1): [(1,0), (-1,0), (0,1)],
    (0,-1):[(1,0), (-1,0), (0,-1)],
}

def solve(input_file: str):
    lines = [[x for x in y] for y in utils.read_lines(input_file)]
    print()

    step = 1
    rotate = 1000
    start = None
    end = None
    walls = set()

    for y, line in enumerate(lines):
        print(str(y).zfill(2), line)
        for x, ch in enumerate(line):
            match ch:
                case "S":
                    start = (y,x)
                case "E":
                    end = (y,x)
                case "#":
                    walls.add((y,x))

    current_pos = start 
    current_facing = (0,1)
    current_score = 0 
    seen = set()

    to_check = defaultdict(list)
    while current_pos != end:
        # print("Pos:", current_pos, "Facing:", current_facing, "Score:",current_score)
        for direction in directions[current_facing]:
            n_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            if n_pos not in walls and (n_pos, direction) not in seen:
                cost = current_score + 1
                if direction != current_facing:
                    cost = current_score + 1001

                to_check[cost].append([cost, n_pos, direction])

        seen.add((n_pos, direction))
        next_score = min(to_check.keys())

        if len(to_check[next_score]) > 0:
            next_item = to_check[next_score].pop()
            # print("- Getting next", next_item)

            current_score = next_item[0]
            current_pos = next_item[1]
            current_facing = next_item[2]
        else: 
            to_check.pop(next_score)
            next_score = min(to_check.keys())
            next_item = to_check[next_score].pop()

            current_score = next_item[0]
            current_pos = next_item[1]
            current_facing = next_item[2]

    print("FOUND END", current_score)
    return current_score