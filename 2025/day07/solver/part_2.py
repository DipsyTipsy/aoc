from solver import utils
from collections import defaultdict

def split_beam(splitters, pos, grid):
    n_beams = []
    for dir in [(0,-1),(0,1)]:
        n_pos = (pos[0]+dir[0], pos[1]+dir[1])
        if n_pos in grid and n_pos not in splitters:
            n_beams.append(n_pos)
    return n_beams

def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]
    splitters = set()
    start = None
    grid = set()
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            grid.add((y,x))
            match c:
                case "S":
                    start = (y,x)
                case "^":
                    splitters.add((y,x))
    beams = defaultdict(int)
    beams[start] = 1
    for i in range(len(lines)):
        n_beams = defaultdict(int)
        for pos, val in beams.items():
            n_pos = (pos[0]+1, pos[1])

            if n_pos in splitters:
                for beam in split_beam(splitters, n_pos, grid):
                    n_beams[beam] += val
            else:
                n_beams[n_pos] +=val
        
        beams = n_beams

    return sum(beams.values())
