from solver import utils
import math
from itertools import combinations
from collections import defaultdict
from shapely import Polygon, Point, box

def area(a,b, tile_ranges, red_tiles, strict=False):
    # print("Calculating Area", a,b)
    min_ = min(a[1], b[1])
    max_ = max(a[1], b[1])
    line = (max_+1 - min_ )
    if line == 1:
        return 0
    for y in range(min(a[0], b[0]), max(a[0], b[0])+1):
        overlap = False
        if all((min_ in range_ and max_ in range_) for range_ in tile_ranges[y]):
                # print("Check ", a,b, "y", y, line, min_, max_)
                overlap = True
        if strict:
            if all(t in range(min_, max_) for t in red_tiles):
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

# def get_range(cur_range, red_tiles, y, polygon):
#     a = cur_range[0]
#     offset = 1
#     continuous = False
#     num_tiles = 1
#     while a + offset in cur_range[offset:]:
#         offset +=1
#         continuous = True
    
#     if continuous:
#         print(y, "is continuous", cur_range, offset, num_tiles)
#         offset -=1

#     n_range = range(a, cur_range[offset]+1)
#     if continuous and offset+1 < len(cur_range):
#         print(y, cur_range[offset+1])
#         if polygon.contains(Point(y, cur_range[offset+1])):
#             print("Inside Polygon")
#             n_range = range(a, cur_range[offset+1]+1)
#         else:
#             cur_range = cur_range[offset+1:]

#     else:
#         cur_range = cur_range[offset+1:]
    
#     print(y, "returning", n_range, cur_range)
#     return (n_range, cur_range)

def update_ranges(ranges):
    old = ranges.copy()
    for j in range(1000):
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
            return

def solve(input_file: str):
    lines = [tuple([int(x) for x in line.split(",")]) for line in utils.read_lines(input_file)]
    tiles = set()
    prev = lines[0]
    red_tiles = set(lines)

    poly = Polygon(lines)
    distances = defaultdict(list)

    for a,b in combinations(red_tiles, 2):
        distances[calc_distance(a,b)].append([a,b])
    
    max_area = 0
    for distance, points in sorted(distances.items(), reverse=True):
        for p_ in points:
            min_x = min(p_[0][0], p_[1][0])
            min_y = min(p_[0][1], p_[1][1])
            max_x = max(p_[0][0], p_[1][0])
            max_y = max(p_[0][1], p_[1][1])

            box_ = box(
                min_x,
                min_y,
                max_x,
                max_y,
                  ) 
            
            if poly.contains(box_):
                dy = (max_y - min_y ) +1
                dx = (max_x - min_x) + 1
                area_ = dy*dx
                # print(p_, box_, dy,dx, area_)
                # print(box_, poly.contains(box_))
                if area_ > max_area:
                    print(box_)
                    max_area = area_

    print(max_area)
    return max_area


    red_tiles = set(lines)
    for a in lines[1:]:
        [tiles.add(tile) for tile in add_between(a, prev)]
        prev = a
    [tiles.add(tile) for tile in add_between(lines[0], prev)]

    tile_ranges = defaultdict(list)

    for tile in tiles:
        tile_ranges[tile[0]].append(tile[1])

    # for key in tile_ranges.keys():
    #     cur_range = sorted(tile_ranges[key])
    #     print(key, ":", cur_range)
    #     ranges = []

    #     while len(cur_range) > 0:
    #         a = cur_range.pop(0)
    #         c =a
    #         print(a)

    # ranges.append(range(a, c+1))
    # tile_ranges[key] = ranges

    total_ranges = 0
    for key in tile_ranges.keys():
        ranges = []
        cur_range = sorted(tile_ranges[key])
        # print(key,":", cur_range, [points for points in red_tiles if points[0]==key])
        window = 2
        for i in range(len(cur_range) - window + 1):
            # print(i, i+1, len(cur_range))
            # print(key, cur_range[i]+1)
            if p.contains(Point(key, cur_range[i]+1)) or cur_range[i]+1 in cur_range:
                ranges.append(range(cur_range[i], cur_range[i+1]+1))
        tile_ranges[key] = ranges
        total_ranges+= len(ranges)
    
    # for key in tile_ranges.keys():
    #     ranges = []
    #     cur_range = sorted(tile_ranges[key])
    #     print(key,":", cur_range)
    #     prev = cur_range[0]
    #     n_range = set()
    #     for val in cur_range[0:]:
    #         if val == prev+1:
    #             n_range.add(val)
    #             n_range.add(prev)
    #             prev = val
    #         else:
    #             if len(n_range) > 0:
    #                 ranges.append(n_range.copy())
    #             n_range = set([val])
    #             prev = val
    #     if len(n_range) > 0:
    #         ranges.append(n_range.copy())
        
    #     print(ranges)
        # tile_ranges[key] = ranges
    
    
#     for key in tile_ranges.keys():
#         cur_range = sorted(tile_ranges[key])
#         print(key, cur_range)
# # 
#         cur_ranges = []
# # 
#         while len(cur_range) > 1:
#             # print(key, cur_range)
#             range_, cur_range = get_range(cur_range, red_tiles, key, p)
#             # print(key, range_)
#             cur_ranges.append(range_)
#         if len(cur_range)==1:
#             cur_ranges.append(range(cur_range[0]-1, cur_range[0]+1))
# # 
#         tile_ranges[key] = cur_ranges
    
    
    print(f"Optimizing Ranges {total_ranges}")
    for y, range_ in tile_ranges.items():
        update_ranges(range_)
        range_ = list(set(range_))
    
    
    distances = defaultdict(list)

    for a,b in combinations(red_tiles, 2):
        distances[calc_distance(a,b)].append([a,b])
    

    area_ = 0
    max_area = 0
    max_points = 0

    for y,range_ in tile_ranges.items():
        print(y, range_)

    print("Finding Max")
    for distance, points in sorted(distances.items(), reverse=True):
        for p_ in points:
            print(p_)
            box(
                min(p_[0][1],p_[1][1]),
                min(p_[0][0],p_[1][0]),
                max(p_[0][1],p_[1][1]),
                max(p_[0][0],p_[1][0]),
                  )
            area_ = area(*p_, tile_ranges, red_tiles)
            if area_ > 0:
                if area_ > max_area:
                    max_area = area_
                    max_points = p_
                    print(max_area)

    print(max_points, max_area)
        
    # for y in range(30):
    #     print(f"{y:02d}", end="")
    #     for x in range(30):
    #         if (y,x) in max_points:
    #             print("0", end="")
    #         elif (y,x) in red_tiles:
    #             print("#", end="")
    #         elif (y,x) in tiles:
    #             print("#", end="")
    #         elif any(x in range_ for range_ in tile_ranges[y]):
    #             print("X", end="")
    #         else:
    #             print(".", end="")
    #     print()
    
    # print(area(*max_points, tile_ranges, red_tiles, True))
    # print(max_points, max_area)
    return max_area

# 66581812
# 187558196
# 113305250
# 2975537880
# 17693016
# 3048773