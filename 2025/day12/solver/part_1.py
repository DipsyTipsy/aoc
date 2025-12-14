from solver import utils
from collections import Counter
import re
from itertools import product
import numpy as np
import copy


def combine_shapes(a,b):
    print(f"Combining\nA:{a}\nB:{b}")
    a_w = len(a[0])
    b_w = len(b[0])

    for offset in range(1,len(a)+1):
        c = []
        works = True
        for a_line, b_line in zip(np.append(a.copy(), np.zeros((a_w, offset)), axis=1), np.append(np.zeros((b_w, offset)),b.copy(), axis=1)):
            c_i = a_line.copy()
            c_i += b_line.copy()
            print(c_i, a_line, b_line)
            if max(c_i) <=1:
                works = True
                print("Works")
                c.append(c_i)
            else:
                print("Not works")
                works = False
                break
        
        if works:
            # print(f"Returning C:\n{c}")
            return c
    return None
        
def check_possible(shapes, grid):
    mapping = {"#": 1, ".":0}
    cur_shape = [np.array([mapping[x] for x in line]) for line in shapes[0].split("\n")]
    print()
    for shape in shapes[1:]:
        print("Current", len(cur_shape), cur_shape, shape)
        # if len(cur_shape) < 1:
        #     return False
        shape_ = [np.array([mapping[x] for x in line]) for line in shape.split("\n")]
        cur_shape = combine_shapes(cur_shape, shape_)
        if not cur_shape:
            return False

    if cur_shape:
        print("Result Shape", cur_shape)
        return True
    else:
        return False

def all_at_once(to_place,grid, presents):
    cur_presents = []
    abs_min_val = []
    # print(grid)

    min_val = 0
    max_val = 0
    num_pos = 0
    can_fit = 0


    for idx, count in enumerate(to_place):
        if count > 0:
            present,area,counts,positions,combos,all_mat = presents[idx]
            # print()
            # print("Adding Present", idx,"x", count)
            # print("\n".join(present))

            # print(positions)
            positions_ = positions.copy()
            min_val_pos = np.min(positions_[positions_ > 0])
            max_val +=  np.max(positions_[positions_ > 0])*count
            for i in range(count-1):
                positions_ += positions
            # print()
            # print(positions_)
            # print("Combo stats", combos, count, combos*count)
            # print("Min",min_val_pos,count, combos, min_val_pos*count*combos)
            # print("Spots", counts["#"], count, counts["#"]*count)
            min_val +=  min_val_pos*count
            # min_val +=  min_val_pos
            # min_val +=  combos*count
            num_pos += counts["#"]*count
            # num_pos += count

            cur_presents.append(positions_.copy())
    # continue
    
    # print()
    print("Total Min:",min_val)
    print("Total Max:",max_val)

    # print(cur_presents)
    # if num_pos > 100:
    #     return
    num_placements = 0
    for present in cur_presents:
        # if min_val > 200:
        #     print()
        #     print(present)
        #     return
        x_size = len(present[0])
        y_size = len(present)
        dy = len(grid) - y_size
        dx = len(grid[0]) - x_size

        num_placements = 0
        for y in range(dy+1):
            for x in range(dx+1):
                grid[y:y+y_size, x:x+x_size] += present
                num_placements += 1

            # if min_val > 200:
            #     print(present)
            #     print(grid)
            #     return
                # print()
                # print(grid[y:y+y_size, x:x+x_size])

    print(grid)
    print("Total pos", num_pos)
    # print("Min val", np.min(grid))
    print("Num Placements",  num_placements)
    # print("Num Placements x min",  num_placements*min_val)

    test_limit = 8*sum(to_place)
    # test_limit = len(grid[0])*len(grid)*8
    # test_limit = ((len(grid[0])*len(grid)))
    spots_under_limit = len(grid[grid < test_limit])
    print("Limit to test",test_limit)
    print("Spots under limit", spots_under_limit)
    abs_min_val.append(np.min(grid))


    # print("Spots under limit", len(grid[grid == min_val]))
    # print("Spots over limit", len(grid[grid > min_val]))
    print("Spots under summed max", len(grid[grid <= max_val]))
    print("Summed Max", max_val)
    print(sum(to_place), sum(to_place)*8)
    # if np.any(grid[grid <= min_val]):
    # if min_val <= len(grid[grid < min_val]):
    if num_pos <= spots_under_limit:
        # print("Can fit")
        print("Can fit")
        can_fit +=1
    print()
    # return
    return can_fit

def check_add(next, presents, cur_grid, queue, visited):
    for idx, count in enumerate(next):
        if count > 0:
            print(len(queue), len(visited))
            left_to_place = copy.deepcopy(next)
            left_to_place[idx] -= 1
            present,area,counts,positions,combos,all_mat = presents[idx]
            for test in all_mat:
                # print(test)
    
                x_size = len(test[0])
                y_size = len(test)
                dy = len(cur_grid) - y_size
                dx = len(cur_grid[0]) - x_size


                for y in range(dy+1):
                    for x in range(dx+1):
                        test_grid = copy.deepcopy(cur_grid)
                        test_grid[y:y+y_size, x:x+x_size] += test
                        # print()
                        # print()
                        # print(cur_grid)
                        # print()
                        # print(test_grid)
                        if len(test_grid[test_grid  > 1]) or str(test_grid) in visited:
                            # print("Overlap")
                            break
                        else:
                            if sum(left_to_place) > 0:
                                # print("Adding to queue")
                                visited.add(str(test_grid))
                                queue.append((left_to_place, test_grid.copy()))
                            else:
                                print()
                                print(left_to_place)
                                print(test_grid)
                                print(len(test_grid[test_grid>0]))
                                print("CAN FIT")
                                return True
    return False

@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)
    mapping = {"#": 1, ".":0}

    presents = []
    trees = []
    object = []
    for line in lines:
        object.append(line)
        if line == "" or "x" in line:
            if "x" in line:
                nums = re.match(r"^(\d+)x(\d+)", line)
                ty,tx = map(int, nums.groups())

                grid = np.zeros((tx,ty))
                target = [int(x) for x in line.split(":")[-1].split(" ") if len(x) > 0]
                trees.append(((ty,tx),target, grid))
            else:
                area = len(object) * len(object[0])
                position =  object[1:-1]
                # positions = set()
                positions = []
                rev_position = ["".join(reversed(x)) for x in position]
                positions.append("\n".join(position))
                positions.append("\n".join(rev_position))
                for i in range(3):
                    position = ["".join(x) for x in list(zip(*position[::-1]))]
                    rev_position = ["".join(reversed(x)) for x in position]
                    # print("adding\n", "\n".join(position), "\nreversed\n", "\n".join(rev_position))
                    positions.append("\n".join(position))
                    positions.append("\n".join(rev_position))
                print("All Positions", positions)
                num_combos = len(positions)
                present_ = list(positions)
                total = np.zeros((len(present_[0].split("\n")), len(present_[0].split("\n")[0]) ))
                all_mat = []
                for shape in present_:
                    cur_shape = [np.array([mapping[x] for x in line]) for line in shape.split("\n")]
                    print(cur_shape)
                    all_mat.append(cur_shape)
                    total +=  cur_shape
                # total[total > num_combos] = 0
                # total[total < num_combos] = 0
                print("Total: ", total)

                presents.append((object[1:-1], area, Counter("".join(object[1:-1])), total.copy(), num_combos, all_mat))
            object = []
        print(line)
    
    can_fit = 0
    for space, to_place, grid in trees:
        print()
        print("Filling Tree", space, to_place)

        # print(to_place)
        queue = [(to_place.copy(), grid.copy())]
        visited = set()

        all_at_once(to_place, grid, presents)

        # while len(queue) > 0:
        #     # print(len(queue))
        #     next, cur_grid = queue.pop()
        #     if check_add(next, presents, cur_grid, queue, visited):
        #         can_fit +=1
        #         break