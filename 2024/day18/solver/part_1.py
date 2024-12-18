from solver import utils
from collections import defaultdict

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def solve(input_file: str, grid_size: int, num_falls):
    lines = [(int(x.split(",")[0]),int(x.split(",")[1])) for x in utils.read_lines(input_file)][:num_falls]
    grid = [["." for x in range(grid_size)] for y in range(grid_size)]
    print()

    for y, line in enumerate(grid):
        print(y, end=" ")
        for x, ch in enumerate(line):
            if (x,y) in lines:
                print("#", end="")
            else:
                print(ch, end="")
        print()
    
    current_position = (0,0)
    goal = (grid_size-1, grid_size-1)

    depth = 0
    queue = defaultdict(list)

    visited = set()
    path = []
    while current_position != goal:
        print(current_position, depth)
        visited.add(current_position)
        for dir in directions:
            n_pos = (current_position[0]+dir[0], current_position[1]+dir[1])
            if all(x in range(grid_size) for x in n_pos) and n_pos not in visited and n_pos not in lines:
                queue[depth+1].append((n_pos, path+[n_pos]))

        depth = min(queue.keys())
        if queue[depth]:
            current_position, path = queue[min(queue.keys())].pop()
        else:
            queue.pop(depth)
            depth = min(queue.keys())
            current_position, path = queue[min(queue.keys())].pop()

        if current_position in visited:
            depth = min(queue.keys())
            if queue[depth]:
                current_position, path = queue[min(queue.keys())].pop()
            else:
                queue.pop(depth)
                depth = min(queue.keys())
                current_position, path = queue[min(queue.keys())].pop()

    for y, line in enumerate(grid):
        print(y, end=" ")
        for x, ch in enumerate(line):
            if (x,y) in lines:
                print("#", end="")
            elif (x,y) in path:
                print("0", end="")
            else:
                print(ch, end="")
        print()
    print(len(path), len(grid), grid_size, num_falls)
    return len(path)