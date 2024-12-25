from solver import utils
from collections import defaultdict

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

    

def solve(input_file: str, min_save = 1):
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
    
    current = start
    current_depth = 0
    path = [(999,999)]*shortest_path
    depths = defaultdict(int)

    for i in range(shortest_path):
        next = [x for x in get_adj(current, lines) if x in avail and x not in path and x != start][0]
        path[i] = current
        current = next

    path.append(end)
    
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
    for pos in fastest_path:
#        print("Current index", fastest_path.index(pos), pos)
        cur_index = fastest_path.index(pos)

        relevant_dir = [x[0] for x in get_adj(pos, lines, return_dir=True) if x[1] in walls]

        adj = [x for x in get_adj(pos, lines, 2, direction=relevant_dir) if x in fastest_path and fastest_path.index(x) > cur_index ]

        for cheat in adj:
            time_saved = (fastest_path.index(cheat) - cur_index)-2 
            if time_saved >= min_save:
                print("- Cheat found", cheat, "Time saved", time_saved, min_save)
                cheats[time_saved].append((pos,cheat))
    
    total_cheats = set()
    for save, cheat in cheats.items():
#        print(len(cheat), save, cheat)
        for pos in cheat:
            total_cheats.add(pos)

    print(len(total_cheats))
    return len(total_cheats)

    def slow():
        paths_to_end = []
        fastest_legal = 99999
        while len(queue) > 0:
            if len(path) > fastest_legal:
                current, current_depth, path, wall_count = queue.pop(0)
                continue

            if current == end:
                print("Found end", wall_count, len(path))
                paths_to_end.append((wall_count, path))
                if wall_count == 0 and len(path) < fastest_legal:
                    fastest_legal = len(path) - 1

                current, current_depth, path, wall_count = queue.pop(0)
                continue

            for pos in get_adj(current, lines):
                _wall_count =  wall_count
                if pos in walls:
                    _wall_count += 1

                if _wall_count < 2 and pos not in path:
                    queue.append((pos, current_depth+1, path+[current], _wall_count))
                    depths[pos] = current_depth+1
            
            seen.add(current)
            current, current_depth, path, wall_count = queue.pop(0)
            print(len(paths_to_end), fastest_legal, current_depth, len(queue), current)

        for y, line in enumerate(lines):
            print(str(y).zfill(2), end=" ")
            for x, ch in enumerate(line):
                if (y,x) in path:
                    print("O", end="")
                else:
                    print(ch, end="")
            print()


        cheats = set()
        for path in paths_to_end:
            print(path[0], len(path[1])-1)
            if len(path[1]) - 1 < fastest_legal - 100:
                for y, line in enumerate(lines):
                        #print(str(y).zfill(2), end=" ")
                        for x, ch in enumerate(line):
                            if (y,x) in path[1] and (y,x) in walls:
                                cheats.add((y,x))

        print(fastest_legal)

        return len(cheats)