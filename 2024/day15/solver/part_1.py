from solver import utils
import time

def move(pos, dir, walls, boxes):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])

    if n_pos in walls:
#        print("- WALL")
        n_pos = pos
    elif n_pos in boxes:
#        print("- BOX")
        if not shove(n_pos, dir, boxes, walls):
            n_pos = pos

    return n_pos

def shove(pos, dir, boxes, walls):
    n_pos = (pos[0]+dir[0], pos[1]+dir[1])
    if n_pos in walls:
#        print("- Not Moving box")
        return False
    elif n_pos in boxes:
#        print("- Collision")
        if shove(n_pos, dir, boxes, walls):
            boxes.remove(pos)
            boxes.add(n_pos)
            return True

    else:
#        print("- Moving box")
        boxes.remove(pos)
        boxes.add(n_pos)
        return True

def draw_grid(pos, boxes,walls, grid):
    for y, line in enumerate(grid):
        print(y,"", end="")
        for x, ch in enumerate(line):
            if (y,x) in boxes:
                print("O", end="")
            elif (y,x) in walls:
                print("#", end="")
            elif (y,x) == pos:
                print("@", end="")
            else:
                print(".", end="")
        print()
 

def solve(input_file: str):
    grid, operations = utils.read_lines(input_file).split("\n\n")
    grid = grid.split("\n")
    operations = operations.replace("\n","")
    print()

    current_pos = None
    boxes = set()
    walls = set()
    for y, line in enumerate(grid):
        print(y, line)
        for x, ch in enumerate(line):
            match ch:
                case "@":
                    current_pos =  (y,x)
                case "O":
                    boxes.add((y,x))
                case "#":
                    walls.add((y,x))
    # print("\033[2J")
    print(len(operations))
    for i, command in enumerate(operations):
        print(i, command)
        match command:
            case "^":
                dir = (-1,0)
            case ">":
                dir = (0,1)
            case "v":
                dir = (1,0)
            case "<":
                dir = (0,-1)

        # print("moving", command, current_pos, dir)
        current_pos = move(current_pos, dir, walls, boxes)
#        print("\033[H")
#        time.sleep(0.1)
    

    draw_grid(current_pos, boxes, walls, grid)
    total = 0
    for box in boxes:
        total += 100*box[0] + box[1]
    
           


    print(total)
    return total