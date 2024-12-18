from solver import utils
from collections import defaultdict

directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]


def solve(input_file: str, grid_size: int, start_check):
    lines = [(int(x.split(",")[0]),int(x.split(",")[1])) for x in utils.read_lines(input_file)]
    grid = [["." for x in range(grid_size)] for y in range(grid_size)]
    print()

    def find_exit(lines, num_falls):
        current_position = (0,0)
        lines = lines.copy()[:num_falls]
        goal = (grid_size-1, grid_size-1)

        depth = 0
        queue = defaultdict(list)

        visited = set()
        path = []
        while current_position != goal:
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
                if not queue.keys():
                    return (None, lines[-1])
                depth = min(queue.keys())
                current_position, path = queue[min(queue.keys())].pop()

            if current_position in visited:
                depth = min(queue.keys())
                if queue[depth]:
                    current_position, path = queue[min(queue.keys())].pop()
                else:
                    queue.pop(depth)
                    if not queue.keys():
                        return (None, lines[-1])
                    depth = min(queue.keys())
                    current_position, path = queue[min(queue.keys())].pop()

        return (len(path), lines[-1])
    
    last_byte = None
    for i in range(start_check, len(lines)):
         print("Checking", i, end=" ")
         s_path, last_byte = find_exit(lines, i)
         if s_path:
             print("- Found path", s_path)
         else:
             print("found no solution")
             print(last_byte)
             break
    
    return last_byte