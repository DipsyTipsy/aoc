from solver import utils

def split_beam(splitters, pos, grid):
    n_beams = set()
    for dir in [(0,-1),(0,1)]:
        n_pos = (pos[0]+dir[0], pos[1]+dir[1])
        if n_pos in grid and n_pos not in splitters:
            n_beams.add(n_pos)
    return list(n_beams)

def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]
    print()
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
    cur_pos = [start]
    cur_dir = (1, 0)
    hit_splitters = set()
    for i in range(len(lines)):
        n_cur_pos = set()
        for pos in cur_pos:
            n_pos = (pos[0]+cur_dir[0], pos[1]+cur_dir[1])
            if n_pos in splitters:
                hit_splitters.add(n_pos)
                r_split = split_beam(splitters, n_pos, grid)
                if len(r_split) > 0:
                    for beam in r_split:
                        n_cur_pos.add(beam)
            else:
                n_cur_pos.add(n_pos)
        cur_pos = list(n_cur_pos)
    
    return len(hit_splitters)
    


