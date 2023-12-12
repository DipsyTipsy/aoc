from solver import utils
from shapely import geometry
import numpy as np
import math
import matplotlib.pyplot as plt


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

                links[(y, x)] = pos_links
            if chr == "S":
                start = (y, x)

    positions = []
    for pos, link in links.items():
        if start in link:
            positions.append([start, pos])
    steps = 1

    main_loop = [start]
    corners = [start]
    while positions[0][1] != start and steps < 100000:
        for i, position in enumerate([positions[0]]):
            for link in links[position[1]]:
                if link != position[0]:
                    next_step = link
            main_loop.append(positions[i][1])
            if not lines[positions[i][1][0]][positions[i][1][1]] in ["|", "-"]:
                corners.append(positions[i][1])
            positions[i][0] = positions[i][1]
            positions[i][1] = next_step

        steps += 1
    corners.append(start)

    main_y, main_x = zip(*corners)

    # trying to shrink
    shrink_factor = 0.72788 / len(lines)

    x_center = 0.5 * min(main_x) + 0.5 * max(main_y)
    y_center = 0.5 * min(main_y) + 0.5 * max(main_x)

    min_corner = geometry.Point(min(main_x), min(main_y))
    max_corner = geometry.Point(max(main_x), max(main_y))
    center = geometry.Point(x_center, y_center)
    shrink_distance = center.distance(min_corner) * shrink_factor

    new_corners = geometry.Polygon(corners).buffer(
        -shrink_distance, cap_style="flat", join_style="mitre", mitre_limit = 2
    )

    plt.figure()
    plt.plot(main_x, main_y)
    plt.plot(main_x, main_y)
    plt.savefig("polygon_original")

    main_y, main_x = new_corners.exterior.xy

    def PolyArea(x, y):
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    area = math.floor(PolyArea(main_x, main_y))
    plt.figure()
    plt.plot(main_x, main_y)
    plt.plot(main_x, main_y)
    plt.savefig("polygon")
    print(len(lines), len(lines[0]))
    print(area)
    return area
