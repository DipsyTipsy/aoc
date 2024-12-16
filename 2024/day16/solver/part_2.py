from solver import utils
from collections import defaultdict

directions = {
    (1,0): [(0,-1), (0, 1), (1,0)],
    (-1,0): [(0,-1), (0,1), (-1,0)],
    (0,1): [(1,0), (-1,0), (0,1)],
    (0,-1):[(1,0), (-1,0), (0,-1)],
}

def solve(input_file: str):
    lines = [[x for x in y] for y in utils.read_lines(input_file)]
    print()

    step = 1
    rotate = 1000
    start = None
    end = None
    walls = set()

    for y, line in enumerate(lines):
        print(str(y).zfill(2), line)
        for x, ch in enumerate(line):
            match ch:
                case "S":
                    start = (y,x)
                case "E":
                    end = (y,x)
                case "#":
                    walls.add((y,x))

    current_pos = start 
    current_facing = (0,1)
    current_score = 0 
    current_path = [current_pos]
    visited = set()
    score_at_end = 0
    seen = defaultdict(int)

    to_check = defaultdict(list)
    nodes_to_end = set()
    
    
    while True:
        print("Pos:", current_pos, "Facing:", current_facing, "Score:",current_score, "Pathlen", len(current_path))
        if current_pos == end:
            #print("- FOUND ENDING")
            score_at_end = current_score
            for path in current_path:
                nodes_to_end.add(path)
        
        if score_at_end > 0 and current_score > score_at_end:
            break
        for direction in directions[current_facing]:
            n_pos = (current_pos[0]+direction[0], current_pos[1]+direction[1])
            if n_pos not in walls and n_pos not in current_path and seen[n_pos] < 100:
                cost = current_score + 1
                if direction != current_facing:
                    cost = current_score + 1001
                
                to_check[cost].append([cost, n_pos, direction, current_path+[n_pos]])


        visited.add(current_pos)
        seen[current_pos] +=1
        next_score = min(to_check.keys())

        if len(to_check[next_score]) > 0:
            next_item = to_check[next_score].pop()
            current_score = next_item[0]
            current_pos = next_item[1]
            current_facing = next_item[2]
            current_path = next_item[3]
        else: 
            to_check.pop(next_score)
            next_score = min(to_check.keys())
            next_item = to_check[next_score].pop()

            current_score = next_item[0]
            current_pos = next_item[1]
            current_facing = next_item[2]
            current_path = next_item[3]

    #print("FOUND END", score_at_end, len(visited))
    for y, line in enumerate(lines):
        print(str(y).zfill(2), end=" ")
        for x, ch in enumerate(line):
            if (y,x) in visited:
                print("0", end="")
            else:
                print(ch, end="")
        print()

    print(nodes_to_end, len(nodes_to_end))
    return len(nodes_to_end)

