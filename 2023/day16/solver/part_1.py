from solver import utils
from collections import defaultdict
import time

def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]
    print()

    up = utils.Pos(-1,0)
    down = utils.Pos(1,0)
    right = utils.Pos(0,1)
    left = utils.Pos(0,-1)

    current_pos = utils.Pos(0, -1)
    current_dir = right

    beams = [[current_pos, current_dir]]

    energized_tiles = []

    # for line in lines:
    #     print(line)

    print("Beams")
    for beam in beams:
        print(beam)
    
    new_grid = [[x for x in y] for y in lines]
    nlines = len(new_grid)
    print(f"\033[{nlines}S", end="")

    # move cursor back up
    print(f"\033[{nlines}A", end="")

    print("\nStarting Loop")
    # save current cursor position
    print("\033[s", end="")

    prev_positions = defaultdict(int)
    for i in range(10000):

        print(len(beams))
        found = []
        for beam in beams:
            beam_pos = (beam[0].x, beam[0].y, beam[1].x, beam[1].y)
            
            found.append(prev_positions[beam_pos] > 1)
        
        for beam in beams:
            key = (beam[0].x, beam[0].y, beam[1].x, beam[1].y)
            prev_positions[key] += 1
        
        print("All seen states", all(found))
        if all(found):
            break
         
        for j, beam in enumerate(beams):
            new_pos = beam[0] + beam[1]
            new_dir = beam[1]
               

            if new_pos.x in range(len(lines[0])) and new_pos.y in range(len(lines)):
                new_chr = lines[new_pos.y][new_pos.x] 
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

        print("\033[u", end="")
        print(f"Loop:{i} Beam:{j}: {beam[0]}{beam[1]} -> {new_pos}{new_dir} {new_chr}                        ", flush=True)
        print(f"Current iterations {i}")
        for line in new_grid:
            print(str("".join(line)))
            # for tile in line:
            #     if tile == "#":
            #         energized_tiles.append(tile)
        # time.sleep(0.01)

    print()
    for line in new_grid:
        print(str("".join(line)))
        for tile in line:
            if tile == "#":
                energized_tiles.append(tile)

    # for beam in beams:
    #     beam_pos = (beam[0].x, beam[0].y, beam[1].x, beam[1].y)
    #     print(beam_pos,  beam_pos in prev_positions)
    
    return len(energized_tiles)
    # print(len(energized_tiles))
    