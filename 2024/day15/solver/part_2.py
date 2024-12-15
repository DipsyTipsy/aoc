from solver import utils
from copy import deepcopy
import time

def move(pos, dir, walls, boxes, big_box):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])

    if n_pos in walls:
        print("- WALL")
        n_pos = pos
    elif n_pos in boxes:
        print("- BOX")
        if not shove(n_pos, dir, boxes, walls, big_box):
            n_pos = pos

    return n_pos

def shove(pos, dir, boxes, walls, big_box):
    current_box = big_box[pos]
    new_box = (
        (current_box[0][0]+dir[0], current_box[0][1]+dir[1]),
        (current_box[1][0]+dir[0], current_box[1][1]+dir[1]),

    )
    collision_boxes = set()
    for pos in new_box:
        if pos in boxes and pos not in current_box:
            collision_boxes.add(big_box[pos])

    if any(n_pos in walls for n_pos in new_box):
        print("- Not Moving box")
        return False
    elif len(collision_boxes) > 0:
        print("- Collision")
        pushes = []
        for box in collision_boxes:
            print("- Trying push", box)
            pushes.append(shove(box[0], dir, deepcopy(boxes), walls, deepcopy(big_box)))

        if all(pushes):
            for box in collision_boxes:
                print("- Doing push", box)
                pushes.append(shove(box[0], dir, boxes, walls, big_box))

            for part in current_box:
                boxes.remove(part)
                big_box.pop(part)

            for part in new_box:
                boxes.add(part)
            big_box[new_box[0]] = new_box
            big_box[new_box[1]] = new_box
            return True
        else:
            print("Fuck")

    else:
        print("- Moving box")
        for part in current_box:
            boxes.remove(part)
            big_box.pop(part)
        for part in new_box:
            boxes.add(part)
        big_box[new_box[0]] = new_box
        big_box[new_box[1]] = new_box
        return True

def draw_grid(pos, boxes,walls, grid, big_box):
    for y, line in enumerate(grid):
        print(y,"", end="")
        for x, ch in enumerate(line):
            if (y,x) in boxes:
                if (y,x) == big_box[(y,x)][0]:
                    print("[", end="")
                else:
                    print("]", end="")

            elif (y,x) in walls:
                print("#", end="")
            elif (y,x) == pos:
                print("@", end="")
            else:
                print(".", end="")
        print()
 

def solve(input_file: str):
    grid, operations = utils.read_lines(input_file).split("\n\n")
    grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid = grid.split("\n")
    operations = operations.replace("\n","")
    print()

    current_pos = None
    boxes = set()
    big_box = {}
    walls = set()
    for y, line in enumerate(grid):
        print(y, line)
        for x, ch in enumerate(line):
            match ch:
                case "@":
                    current_pos =  (y,x)
                case "[":
                    boxes.add((y,x+1))
                    boxes.add((y,x))
                    big_box[(y,x)] = ((y,x),(y,x+1))
                    big_box[(y,x+1)] = ((y,x),(y,x+1))
                case "#":
                    walls.add((y,x))
    # print("\033[2J")
    print(len(operations))
    for i, command in enumerate(operations):
        # print(i, command)
        match command:
            case "^":
                dir = (-1,0)
            case ">":
                dir = (0,1)
            case "v":
                dir = (1,0)
            case "<":
                dir = (0,-1)

        print("moving", command, current_pos, dir)
        current_pos = move(current_pos, dir, walls, boxes, big_box)
    

    draw_grid(current_pos, boxes, walls, grid, big_box)
    total = 0
    actual_boxes = set(box for box in big_box.values())
    for box in actual_boxes:
        total += 100*box[0][0] + box[0][1]
    
    print(len(actual_boxes), len(actual_boxes)*2, len(big_box), len(boxes))
    
           
    print(total)
    return total
    # 1445725 is too high