from solver import utils
import math

def solve(input_file: str, steps: int):
    lines = [list(x) for x in utils.read_lines(input_file)]
    bounds = (len(lines), len(lines[0]))
    print()

    start = None

    nodes = {}
    dirs = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
    }

    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr == "S":
                start = (y, x)
            if chr in ["S", "."]:
                possible_dirs = []
                for dir in dirs.values():
                    new_pos = (y + dir[0], x + dir[1])
                    if new_pos[0] < bounds[0] and new_pos[0] >= 0 and new_pos[1] < bounds[1] and new_pos[1] >= 0:
                        if lines[new_pos[0]][new_pos[1]] in ["S", "."]:
                            possible_dirs.append(new_pos)
                    else:
                        possible_dirs.append(new_pos)


                nodes[(y,x)] = possible_dirs


    for line in lines:
        print(line)

    print(f"{start=}")
    for node in nodes.items():
        print(node)

    positions = set()
    positions.add((start, (0,0)))
    for i in range(steps):
        print(f"\rCycle {i}: {len(positions)=}", end="")

        next_round = set()
        for node in positions:
            new_pos = node[0]
            box_y = math.floor(new_pos[0]/bounds[0])
            box_x = math.floor(new_pos[1]/bounds[1])
            norm_x = new_pos[1] % bounds[1]
            norm_y = new_pos[0] % bounds[0]

            print(norm_y, norm_x)
            normalized_pos = (norm_y, norm_x)
            print(new_pos, normalized_pos, (box_y, box_x))

            for neighbour in nodes[normalized_pos]:
                next_round.add((neighbour, (box_y, box_x)))
        positions = next_round

    print()
    for position in positions:
        print(position)
    
    return len(positions)

