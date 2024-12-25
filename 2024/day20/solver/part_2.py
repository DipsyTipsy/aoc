from solver import utils
from collections import defaultdict
import numpy as np

directions = [(1,0), (-1, 0), (0,1), (0,-1)]

def get_adj(pos, grid, scale = 1, direction = directions, return_dir = False):
    adj = []
    for dir in direction:
        n_pos = (pos[0]+dir[0]*scale, pos[1]+dir[1]*scale)
        if all(x in range(len(grid)) for x in n_pos):
            if return_dir:
                adj.append((dir, n_pos))
            else:
                adj.append(n_pos)
    return adj

def solve(input_file: str, min_save = 50):
    lines = [ x for x in utils.read_lines(input_file)]
    print()

    start = None
    end = None
    walls = set()
    avail = set()

    shortest_path = 0
    for y, line in enumerate(lines):
        print(str(y).zfill(2), line)
        for x, ch in enumerate(line):
            match ch:
                case "S":
                    start = (y,x)
                case "E":
                    end = (y,x)
                    shortest_path += 1
                    avail.add((y,x))
                case "#":
                    walls.add((y,x))
                case ".":
                    shortest_path += 1
                    avail.add((y,x))
    
    
    path = [(999,999)]*shortest_path
    current = start

    for i in range(shortest_path):
        next = [x for x in get_adj(current, lines) if x in avail and x not in path and x != start][0]
        path[i] = current
        current = next

    path.append(end)
    path = np.array(path)
    
    fastest_path = path
    print("\nFastest path: ",  len(fastest_path))
    for y, line in enumerate(lines):
        print(str(y).zfill(2), end=" ")
        for x, ch in enumerate(line):
            if (y,x) in path:
                print("O", end="")
            else:
                print(" ", end="")
        print()
    
    cheats = defaultdict(list)
    for i, pos in enumerate(fastest_path):
        for j, o_pos in enumerate(fastest_path[i+min_save:]):
            #delta = abs(o_pos[0] - pos[0]) + abs(o_pos[1] - pos[1])
            delta = np.abs(o_pos - pos).sum()
            time_saved = j+min_save - delta
            if time_saved >= min_save and delta <= 20:
                    print(i,"/", len(fastest_path), "- Posisble timesave of", time_saved, pos,"->", o_pos, "Delta:",delta)
                    cheats[time_saved].append(str((pos, o_pos)))
                    #if any(move(pos, o_pos, lines, walls, delta)):
                    #    cheats[time_saved].append(str((pos, o_pos)))
                    #else: 
                    #    print("- Not good")

                    for y, line in enumerate(lines):
                        print(str(y).zfill(2), end=" ")
                        for x, ch in enumerate(line):
                            if all((y,x) == pos):
                                print("1", end="")
                            elif all((y,x) == o_pos):
                                print("2", end="")
                            else:
                                print(ch, end="")
                        print()
    

    total_cheats = set()
    for save, cheat in cheats.items():
        print("#Cheats", len(cheat), "timesave:", save)
        for pos in cheat:
            total_cheats.add(pos)


    print(len(total_cheats))
    # return len(total_cheats)

def move(pos, o_pos, lines, walls, delta):
    current = pos
    seen = set()
    queue = [x for x in get_adj(pos, lines) if x in walls]
    path=[current]

    while len(queue) > 0:
        if len(path) > delta:
            seen.add(str(current))
            current, path = queue.pop()

        if all(current == o_pos):
            # for y, line in enumerate(lines):
            #     print(str(y).zfill(2), end=" ")
            #     for x, ch in enumerate(line):
            #         if (y,x) == pos:
            #             print("1", end="")
            #         elif (y,x) == o_pos:
            #             print("2", end="")
            #         elif (y,x) in path:
            #             print("0", end="")
            #         else:
            #             print(ch, end="")
            #     print()
    
            return o_pos
        
        for adj in [np.array(x) for x in get_adj(current, lines) if (x in walls and str(np.array(x)) not in seen) or all(x == o_pos)]:
            queue.append((adj, np.append(path, [current], axis=0)))
        
        seen.add(str(current))
        current, path = queue.pop()
        print(current,path)
    
    print("Fack")
    
    return False