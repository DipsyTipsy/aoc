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
            for pos in positions:
                area += 1
                print(pos)
            print(area, sides)
            total_price += area*sides

    return total_price