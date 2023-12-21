from solver import utils


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

                nodes[(y,x)] = possible_dirs


    # for line in lines:
    #     print(line)

    # print(f"{start=}")
    # for node in nodes.items():
    #     print(node)

    positions = set()
    positions.add(start)
    for i in range(steps):
        print(f"\rCycle {i}: {len(positions)=}", end="")

        next_round = set()
        for node in positions:
            for neighbour in nodes[node]:
                next_round.add(neighbour)
        positions = next_round

    # print()
    # print(positions)
    
    # for y, line in enumerate(lines):
    #     for x, chr in enumerate(line):
    #         if (y,x) in positions:
    #             print("O", end="")
    #         else:
    #             print(chr, end="")
    #     print()

    return len(positions)