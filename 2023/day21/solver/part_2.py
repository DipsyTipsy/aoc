from solver import utils
from collections import defaultdict
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
                            possible_dirs.append(dir)
                    else:
                        possible_dirs.append(dir)


                nodes[(y,x)] = possible_dirs


    for line in lines:
        print(line)

    print(f"{start=}")
    # for node in nodes.items():
    #     print(node)

    positions = set()
    positions.add((start, (0,0)))
    current_bounds = defaultdict(list)
    completed_bound = {}
    for i in range(steps):
        print(f"\rSteps {i}: {len(positions)=} {len(current_bounds)=} {len(completed_bound)=}", end="")
        # guess = i + len(current_bounds) + len(positions)
        # print(f"\t{guess}")

        next_round = set()
        current_bounds_count = defaultdict(int)
        for node in positions:
            current_bounds_count[node[1]] += 1
            new_pos = node[0]
            norm_x = new_pos[1] % bounds[1]
            norm_y = new_pos[0] % bounds[0]

            normalized_pos = (norm_y, norm_x)
            # print(f"POS {new_pos}\tNORM: {normalized_pos}\tSPACE: {node[-1]}")

            for dir in nodes[normalized_pos]:
                child_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1])
                box_y = math.floor(child_pos[0]/bounds[0])
                box_x = math.floor(child_pos[1]/bounds[1])
                # print(f"\tDIR: {dir} CHILD: {child_pos} {(box_y, box_x)}")
                # if not (box_y, box_y) in completed_bound:
                next_round.add((child_pos, (box_y, box_x)))

        for bound, count in current_bounds_count.items():
            current_bounds[bound].append(count)
            if count == 42 and not bound in completed_bound:
                # surrounding_done = []
                # for dir in [(-1,0), (0, 1), (0,-1), (1, 0),(-1, -1), (-1, 1),(1, -1), (1, 1)]:
                #     bound_check = (bound[0]+dir[0], bound[1]+dir[1])
                #     if bound_check in current_bounds:
                #         if current_bounds[bound_check] == 42 or completed_bound.get(bound_check):
                #             # print(completed_bound.get(bound_check))
                #             surrounding_done.append(True)
                #     else:
                #         surrounding_done.append(False)
                #         break
                # if all(surrounding_done):
                    # print("Bound Done:", bound)
                completed_bound[bound] = i

        positions = next_round

        # if len(current_bounds) > 9:
        #     # print(f"\nExceeded space at {i}")
        #     break

    # print()
    # for position in positions:
    #     print(position)

    for bound, count in current_bounds.items():
        print(bound, count[-2:])
    
    
    total_positions = len(positions)

    print("Summary", i, len(completed_bound))

    for bound, step in sorted(completed_bound.items(), key=lambda x: x[1]):
        print(bound, step)
    #     total_positions += 39

    print(len(nodes))

    
    # for y, line in enumerate(lines):
    #     for x, chr in enumerate(line):
    #         if (y,x) in positions:
    #             print("O", end="")
    #         else:
    #             print(chr, end="")
    #     print()

    # return len(positions)

    return total_positions

