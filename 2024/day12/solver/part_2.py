from solver import utils
from collections import defaultdict


def score_plot(pos, plant, garden):
    sides = 1
    return sides

def solve(input_file: str):
    lines = [[x for x in y] for y in utils.read_lines(input_file)]

    print(lines)
    gardens = defaultdict(list)


    seen = set()
    for y, line in enumerate(lines):
        for x, plot in enumerate(line):
            pos  = (y,x)
            if pos in seen:
                continue
            seen.add(pos)
            current_garden = {pos}
            to_check = [(pos[0]+dir[0], pos[1]+dir[1]) for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]]

            while len(to_check) > 0:
                checking = to_check.pop()
                ny = checking[0]
                nx = checking[1]
                if ny in range(len(lines)) and nx in range(len(lines)):
                    if (ny,nx) in seen:
                        continue
                    if plot == lines[ny][nx]:
                        current_garden.add((ny,nx))
                        to_check += [(ny+dir[0], nx+dir[1]) for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
                        seen.add((ny,nx))
            print("plot", plot, current_garden)
            gardens[plot].append(current_garden)
                    
    total_price = 0
    for plant, plots in gardens.items():
        print("plant", plant)
        for positions in plots:
            area = 0 
            sides = 0
            perimiters = defaultdict(list)
            adjacent = defaultdict(list)
            for pos in positions:
                area += 1
                print(pos)

                for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny = pos[0]+dir[0]
                    nx = pos[1]+dir[1]
                    if (ny,nx) not in positions:
                        print(pos, "Perimiter", dir)
                        perimiters[pos].append(dir)
                    else:
                        adjacent[pos].append((ny,nx))
            
            seen = set()
            sides = 0
            for pos in positions:
                for perimiter in perimiters[pos]:
                    side = set()
                    if not (pos, perimiter) in seen:
                        to_check = [pos]
                        cur = pos
                        side.add(cur)
                        while len(to_check) > 0:
                            for adj in adjacent[cur]:
                                if perimiter in perimiters.get(adj,[]) and (adj, perimiter) not in seen:
                                    to_check.append(adj)
                                    print("Found same permiter in adj", adj, perimiter)
                                    side.add(adj)
                            
                            cur = to_check.pop()
                            seen.add((cur, perimiter ))
                    if len(side) > 0:
                        print("Found side", side)
                        sides += 1



            print(area, sides)
            total_price += area*sides

    return total_price