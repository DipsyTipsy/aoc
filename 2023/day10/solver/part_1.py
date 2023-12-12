from solver import utils


def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]
    dimentions = (len(lines), len(lines[0]))
    mapping = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }

    links = {}
    start = ()
    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr in mapping:
                pos_links = []
                for link in mapping[chr]:
                    link_x = link[1] + x
                    link_y = link[0] + y
                    if link_y < dimentions[0] and link_x < dimentions[1]:
                        pos_links.append((link_y, link_x))

                links[(y,x)] = pos_links
            if chr == "S":
                start = (y,x)

    positions = []
    for pos, link in links.items():
        if start in link:
            positions.append([start, pos])
    steps = 1

    while positions[0][1] != positions[1][1] and steps < 100000:
        for i, position in enumerate(positions):
            for link in links[position[1]]:
                if link != position[0]:
                    next_step = link
            positions[i][0] = positions[i][1]
            positions[i][1] = next_step

        steps += 1

    return steps