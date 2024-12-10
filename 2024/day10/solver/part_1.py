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

def solve(input_file: str):
    lines = [[int(y) for y in x] for x in utils.read_lines(input_file)]

    print(lines)

    trail = {}
    trailheads = set()

    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            print(y, x, chr)
            if chr == 0:
                trailheads.add((y,x))
            if chr != ".":
                adj = []
                for dir in [(-1,0), (0,1), (0, -1), (1,0)]:
                    neigh = (y+dir[0], x+dir[1])
                    if neigh[0] in range(len(lines)) and neigh[1] in range(len(lines)):
                        if lines[neigh[0]][neigh[1]] == chr +1:
                            print("Found neighbor", neigh)
                            adj.append(neigh)

                trail[(y,x)] = Position((y,x), int(chr), adj)

    for pos, Trail in trail.items():
        print(pos, Trail)

    scores = 0
    for head in trailheads:
        peaks = set()
        print("Starting from ", head)
        current_positions = set()
        current_positions.add(head)
        while current_positions:
            _current_positions = current_positions.copy()
            for i, pos in enumerate(_current_positions):
                current_positions.remove(pos)
                if trail.get(pos).height == 9:
                    print("Found peak")
                    peaks.add(pos)
                    break
                else:
                    for adj in trail.get(pos).adjacent:
                        current_positions.add(adj)
        scores += len(peaks)

    print(scores)
    return scores