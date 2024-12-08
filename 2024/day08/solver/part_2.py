from solver import utils
from collections import defaultdict
from itertools import permutations 
import numpy as np


def solve(input_file: str):
    lines = [[x for x in y ] for y in utils.read_lines(input_file)]
    print()

    antennas = defaultdict(list)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                antennas[c].append(np.array([y,x]))


    antinodes = set()
    for a_type, positions in antennas.items():
        print(a_type, positions)
        for a, b in permutations(positions, 2):
            vec = a - b

            possible_antinodes = []

            #Okay, this is quite dirty, but it works
            for i in range(1,100):
                possible_antinodes.append(a+vec*i)
                possible_antinodes.append(a-vec*i)
                possible_antinodes.append(b+vec*i)
                possible_antinodes.append(b-vec*i)


            for antinode in possible_antinodes:
                if antinode[0] in range(len(lines)) and antinode[1] in range(len(lines)):
                    antinodes.add((antinode[0], antinode[1]))
                    print("Antinode", antinode)
                    lines[antinode[0]][antinode[1]] = "#"

    for line in lines:
        print("".join(line))
    print(len(antinodes))
    return len(antinodes)
