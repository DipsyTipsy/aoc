from solver import utils
from collections import defaultdict


directions = [
    (1,0),
    (1,1),
    (0,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1, -1),
    (-1, 1)
]


def search(map, y, x, dir, target, hits):
    hit = 0
    try:
        new_y = y + dir[0]
        new_x = x + dir[1]
        if new_y < 0 or new_x < 0:
            return 0
        destination = map[new_y][new_x]
    except IndexError:
        return 0
    if target == destination:
        for hit in hits:
            hits[y][x] = map[y][x]
            hits[new_y][new_x] = destination
            #print("".join(hit))

        if target == "M":
            hit = search(map, new_y, new_x, dir, "A", hits)
        
        if target == "A":
            hit = search(map, new_y, new_x, dir, "S", hits)
        
        if target == "S":
            #print("Found word at", y, x, dir)
            hit = 1
        
        if hit >= 1:
            hits[new_y][new_x] = destination

        return hit
    else:
        return 0



def solve(input_file: str):
    lines = [[y for y in x] for x in utils.read_lines(input_file)]
    total_hits = [["." for x in range(len(lines))] for y in range(len(lines))]
    current_hits = set()
    for line in lines:
        print(line)

    total = 0 
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "X":
                #print("Found X at",y, x, char)
                for dir in directions:
                    hits = [["." for x in range(len(lines))] for y in range(len(lines))]
                    matches = search(lines, y,x,dir,"M",hits)

                    if matches:
                        hits[y][x] = "X"
                        occurance = ""
                        for i, hit in enumerate(hits):
                            #print("".join(hit))
                            occurance += "".join(hit)
                            for j, c in enumerate(hit):
                                if c != ".":
                                    total_hits[i][j] = c
                #        print()

                        if occurance not in current_hits:
                            total += matches
                            current_hits.add(occurance)
    
    print(total)
    for y, hit in enumerate(total_hits):
        print("".join(hit))
    return total