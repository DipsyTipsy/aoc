from solver import utils
from collections import defaultdict

class Position:
    pos = None
    height = None
    adjacent = None

    def __init__(self, pos, height, adjacent = []):
        self.pos = pos
        self.height = height
        self.adjacent = adjacent
        pass
    
    def __repr__(self):
        return f'Position: {self.pos}, Height: {self.height}, Adj: {len(self.adjacent)}'
        pass

def move(pos, trail, walked, trail_counter):
    walked.add(pos)

    if trail.get(pos).height == 9:
        #print("Found peak")
        trail_counter.append(1)
        return walked
    else:
        for adj in trail.get(pos).adjacent:
            move(adj, trail, walked, trail_counter)
    
    return walked


def solve(input_file: str):
    lines = [[int(y) for y in x] for x in utils.read_lines(input_file)]

    print(lines)

    trail = {}
    trailheads = set()

    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            if chr == 0:
                trailheads.add((y,x))
            if chr != ".":
                adj = []
                for dir in [(-1,0), (0,1), (0, -1), (1,0)]:
                    neigh = (y+dir[0], x+dir[1])
                    if neigh[0] in range(len(lines)) and neigh[1] in range(len(lines)):
                        if lines[neigh[0]][neigh[1]] == chr +1:
                            adj.append(neigh)

                trail[(y,x)] = Position((y,x), int(chr), adj)

    #for pos, Trail in trail.items():
    #    print(pos, Trail)

    scores = 0
    for head in trailheads:
        print("Starting from ", head)
        trail_counter = []
        move(head, trail, set(), trail_counter)
        print(head, "Rating", sum(trail_counter))
        scores += sum(trail_counter)

    print(scores)
    return scores