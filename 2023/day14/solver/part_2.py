from solver import utils
import copy, math

class Pos:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Pos(self.y + o.y, self.x + o.x)

    def __str__(self):
        return f"Pos({self.y}, {self.x})"

    def __repr__(self):
        return f"Pos({self.y}, {self.x})"


def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]

    print()
    for line in lines:
        print(line)

    def traverse(pos, dir, grid):
        new_pos = pos + dir
        if new_pos.x in range(len(grid[0])) and new_pos.y in range(len(grid)):
            if grid[new_pos.y][new_pos.x] == ".":
                return traverse(new_pos, dir, grid)
        return pos

    directions = [Pos(-1,0), Pos(0,-1), Pos(1,0), Pos(0,1)]
    num_cycles = 1000000000
    current_cycle = lines.copy()
    print()
    orders = {}
    in_loop = False
    for cycle in range(num_cycles):
        if in_loop:
            break
        for dir in directions:
            sums = []
            new_grid = [[x.replace("O", ".") for x in y] for y in current_cycle]
            num_rocks = 0
            loop_dir = [1,1]
            if dir.x == 1:
                loop_dir[1] = -1
            if dir.y == 1:
                loop_dir[0] = -1
            
            for y in range(len(current_cycle))[::loop_dir[0]]:
                for x in range(len(current_cycle[0]))[::loop_dir[1]]:
                    if current_cycle[y][x] == "O":
                        num_rocks += 1
                        rock = traverse(Pos(y, x), dir, new_grid)
                        # print(y,x," --> ", rock.y, rock.x)
                        new_grid[rock.y][rock.x] = "O"
                        sums.append(len(lines)-rock.y)

            # print("Cycle:", cycle, "Current dir:", dir, "Num rocks", num_rocks)
            # for line in new_grid:
            #     print("".join(line))
            # print(cycle, len(orders), sum(sums))
            # print()
            current_cycle = new_grid
        key = "".join(["".join([x for x in y]) for y in new_grid])
        if key in orders:
            orders[key].append((cycle, sum(sums)))
            if len(orders[key]) == 5:
                print("Loop found")
                in_loop = True
        else:
            orders[key] = [(cycle, sum(sums))]
             
        # print("\nCycle:", cycle)
        # for line in current_cycle:
        #     print("".join(line))
    
    # print(orders.values())
    loop = {} 
    start_of_loop = []
    for order, hits in orders.items():
        if(len(hits) >= 3):
            start_of_loop.append(hits[0][0])
            print(hits[-1])
            loop[hits[-1][0]] = hits[-1][1]
    
    start_of_loop = min(start_of_loop)
    
    loop = sorted(loop.items())
    print((num_cycles - start_of_loop-2) % (len(loop)))
    hit = (num_cycles - start_of_loop-2) % (len(loop))

    return loop[hit][1]