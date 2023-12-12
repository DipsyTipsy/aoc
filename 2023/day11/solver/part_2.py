from solver import utils
from itertools import combinations
import copy


def solve(input_file: str, test: bool):
    lines =[list(x) for x in utils.read_lines(input_file)]

    x_counts = [0] * len(lines[0])
    y_counts = [0] * len(lines)
    galaxies = []

    for y, line in enumerate(lines):
        for x, pos in enumerate(line):
            if pos == "#":
                x_counts[x] +=1
                y_counts[y] +=1
                galaxies.append([y+1, x+1])
    
    expansion_increment = 1000000
    if test:
        expansion_increment = 100
    def cosmic_expansion(space, cosmic_count, axies):
        new_space = copy.deepcopy(space)
        for x, count in enumerate(cosmic_count):
            if count == 0:
                for i, galaxy in enumerate(space):
                    if galaxy[axies] > x:
                        new_space[i][axies] += expansion_increment - 1
        return new_space
    
    print()
    #print(galaxies)
    galaxies = cosmic_expansion(galaxies, y_counts, 0)
    galaxies = cosmic_expansion(galaxies, x_counts, 1)
    #print(galaxies)

    pairs = list(combinations(galaxies, 2))

    paths = []
    for pair in pairs:
        step_x = abs(pair[0][1] - pair[1][1])
        step_y = abs(pair[0][0] - pair[1][0])
        paths.append(step_x+step_y)
                    
    #for line in lines:
    #    print(line)
    
    return sum(paths)




