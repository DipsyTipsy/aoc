from solver import utils
from collections import defaultdict


def score_plot(pos, plant, garden):
    area = 1
    perimiter = 0
    for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny = pos[0]+dir[0]
        nx = pos[1]+dir[1]
        if ny in range(len(garden)) and nx in range(len(garden)):
            if plant == garden[ny][nx]:
                continue
            else:
                perimiter += 1
        else:
            perimiter += 1

    return (area, perimiter)

def solve(input_file: str):
    lines = [[x for x in y] for y in utils.read_lines(input_file)]
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
            gardens[plot].append(current_garden)
                    
    total_price = 0
    for plant, plots in gardens.items():
        for positions in plots:
            area = 0 
            perimiter = 0
            for pos in positions:
                _area, _perimiter = score_plot(pos, plant, lines)
                area += _area
                perimiter += _perimiter
            total_price += area*perimiter

    return total_price


