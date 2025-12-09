from solver import utils
import math
from itertools import combinations
from collections import defaultdict

def area(a,b, tile_ranges, red_tiles, strict=False):
    min_ = min(a[1], b[1])
    max_ = max(a[1], b[1])
    line = (max_+1 - min_ )
    if line == 1:
        return 0
    for y in range(min(a[0], b[0]), max(a[0], b[0])+1):
        overlap = False
        if any((min_ in range_ and max_ in range_) for range_ in tile_ranges[y]):
                # print("Check ", a,b, "y", y, line)
                overlap = True
                break
        if strict:
            if any(t in range(min_, max_) for t in red_tiles):
                print("wtf")
                return 0
        if not overlap:
            # print("Not in", min_, max_, tile_ranges[y])
            return 0
    return line * (max(a[0], b[0])+ 1 - min(a[0], b[0]))

def calc_distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def add_between(a,b):
    tiles_ = set()
    for x in range(min(a[1], b[1]), max(a[1], b[1])):
        tiles_.add((a[0], x))
    for y in range(min(a[0], b[0]), max(a[0], b[0])):
        tiles_.add((y, a[1]))
    tiles_.add(a)
    return tiles_

def get_range(cur_range, red_tiles, y):
    a = cur_range[0]
    offset = 1
    continuous = False
    while a + offset in cur_range[offset:]:
        offset +=1
        continuous = True
    
    if continuous:
        offset -=1

    n_range = range(a, cur_range[offset]+1)
    if continuous and (y, cur_range[offset]) in red_tiles and offset+1 < len(cur_range):
        if not (y, cur_range[offset+1]) in red_tiles:
            # print("WHat", y, cur_range[offset], cur_range, n_range)
            n_range = range(a, cur_range[offset+1]+1)
            cur_range = cur_range[offset+2:]
            # print(n_range)
        else:
            cur_range = cur_range[offset+1:]
    else:
        cur_range = cur_range[offset+1:]
    return (n_range, cur_range)

def update_ranges(ranges):
    old = ranges.copy()
    range_ = ranges.pop(0)
    added = False
    for i, check in enumerate(ranges):
        if (range_.stop >= check.start and check.stop >= range_.start):
            a = min(check.start, range_.start)
            b = max(check.stop, range_.stop)
            check = range(a,b)
            ranges[i] = check
            added = True
            
    if not added:
        ranges.append(range_)
    else:
        print("Changed, from ", old,"to ", ranges )
            # return

@utils.performance_timer
def solve(input_file: str):
    lines = [tuple([int(x) for x in line.split(",")]) for line in utils.read_lines(input_file)]
    tiles = set()
    prev = lines[0]

    red_tiles = set(lines)
    for a in lines[1:]:
        [tiles.add(tile) for tile in add_between(a, prev)]
        prev = a
    [tiles.add(tile) for tile in add_between(lines[0], prev)]

    y_count = defaultdict(int)
    for t in red_tiles:
        y_count[t[0]] +=1


    tile_ranges = defaultdict(list)
    for tile in tiles:
        tile_ranges[tile[0]].append(tile[1])
    
    for key in tile_ranges.keys():
        cur_range = sorted(tile_ranges[key])
        cur_ranges = []

        while len(cur_range) > 1:
            range_, cur_range = get_range(cur_range, red_tiles, key)
            cur_ranges.append(range_)
        if len(cur_range)==1:
            cur_ranges.append(range(cur_range[0]-1, cur_range[0]+1))

        tile_ranges[key] = cur_ranges
    
    
    for y, range_ in tile_ranges.items():
        update_ranges(range_)
        range_ = list(set(range_))
    
    
    distances = defaultdict(list)

    for a,b in combinations(red_tiles, 2):
        distances[calc_distance(a,b)].append([a,b])
    

    area_ = 0
    max_area = 0

    # for y,range_ in tile_ranges.items():
    #     print(y, range_, y_count[y])

    print("Finding Max")
    for distance, points in sorted(distances.items(), reverse=True):
        for p in points:
            area_ = area(*p, tile_ranges, red_tiles)
            if area_ > 0:
                if area_ > max_area:
                    max_area = area_
                    max_points = p
                    print(max_area)
            # if max_area > 0:
            #     return max_area

    print(max_points, max_area)
        
    for y in range(20):
        for x in range(20):
            if (y,x) in max_points:
                print("0", end="")
            elif (y,x) in red_tiles:
                print("#", end="")
            elif any(x in range_ for range_ in tile_ranges[y]):
                print("X", end="")
            else:
                print(".", end="")
        print()
    
    print(area(*max_points, tile_ranges, red_tiles, True))
    print(max_points, max_area)
    return max_area

# 66581812
# 187558196
# 113305250
# 2975537880