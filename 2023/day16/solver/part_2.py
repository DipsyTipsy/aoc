
from solver import utils
from collections import defaultdict
import time, math
up = utils.Pos(-1,0)
down = utils.Pos(1,0)
right = utils.Pos(0,1)
left = utils.Pos(0,-1)


def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]
    print()

    current_pos = utils.Pos(0, -1)
    current_dir = right

    beams_to_try = []

    for beam in [[utils.Pos(y, len(lines[0])-1), left] for y in range(len(lines[0]))]:
        beams_to_try.append(beam)
    for beam in [[utils.Pos(0, x), down] for x in range(len(lines))]:
        beams_to_try.append(beam)
    for beam in [[utils.Pos(len(lines)-1, x), up] for x in range(len(lines))]:
        beams_to_try.append(beam)
    for beam in [[utils.Pos(y, 0), right] for y in range(len(lines[0]))]:
        beams_to_try.append(beam)

    print("Beams to try", len(beams_to_try))

    current_max = 0
    for i, beam in enumerate(beams_to_try):
        print(f"\rBeam number: {i} current_max: {current_max}        ", end="")
        current = run_beam([beam], lines)
        current_max = max(current_max, current)
    print()
    return current_max

    
def run_beam(beams, grid, max_iterations = 1000000):
        energized_tiles = []
        prev_positions = defaultdict(int)

        new_grid = [[x for x in y] for y in grid]
        # print("\nStarting Loop")
        for i in range(max_iterations):
            found = []
            for beam in beams:
                key = (beam[0].x, beam[0].y, beam[1].x, beam[1].y)
                found.append(prev_positions[key] > 2)
                prev_positions[key] += 1
            
            # print("\rAll seen states ", all(found), "", end="")
            if all(found):
                break
            
            for j, beam in enumerate(beams):
                new_pos = beam[0] + beam[1]
                new_dir = beam[1]

                if new_pos.x in range(len(grid[0])) and new_pos.y in range(len(grid)):
                    new_chr = grid[new_pos.y][new_pos.x] 
                    new_grid[new_pos.y][new_pos.x] = "#"
                else:
                    beams.pop(j)
                    continue

                if (new_pos.x, new_pos.y, new_dir) in prev_positions:
                    continue
                
                match new_chr:
                    case "|":
                        if abs(beam[1].x) == 1:
                            new_dir = up
                            beams.append([new_pos, down])
                    case "-":
                        if abs(beam[1].y) == 1:
                            new_dir = left
                            beams.append([new_pos, right])
                    case "/":
                        if new_dir == left:
                            new_dir = down
                        elif new_dir == right:
                            new_dir = up
                        elif new_dir == up:
                            new_dir = right
                        elif new_dir == down:
                            new_dir = left
                    case "\\":
                        if new_dir == left:
                            new_dir = up
                        elif new_dir == right:
                            new_dir = down
                        elif new_dir == down:
                            new_dir = right
                        elif new_dir == up:
                            new_dir = left

                beams[j] = [new_pos, new_dir]

            # print(f"Current iterations {i}", end="")

        # print()
        for line in new_grid:
            for tile in line:
                if tile == "#":
                    energized_tiles.append(tile)
        return len(energized_tiles)
