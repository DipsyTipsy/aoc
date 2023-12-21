from solver import utils

class node():
    def __init__(self, parent=None, position=None, direction=None):
        self.parent = parent
        self.position = position
        self.direction = direction
        # G is the distance between the current node and the start node.
        self.g = 0
        # H is the heuristic — estimated distance from the current node to the end node.
        self.h = 0
        # F is the total cost of the node
        self.f = 0

    def __repr__(self):
        return f"node(positon={self.position},f={self.f})"
    def __eq__(self, other):
        if self.direction and other.direction:
            return all([self.position == other.position, self.direction == other.direction])
        return self.position == other.position
    def __sub__(self, other):
        return (other.position[0] - self.position[0], other.position[1] - self.position[1])

def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]

    print()
    for line in lines:
        print(line)
    
    start = (0,0)
    end = (len(lines)-1, len(lines[0])-1)

    open_list = []
    closedList = []

    startNode = node(None, start)
    end_node = node(None, end)
    open_list.append(startNode)

    failsafe = 0
    path = []
    total_heat = 0

    while len(open_list) > 0:
        failsafe += 1
        current_node = open_list[0]
        currentIndex = 0
        for i, sel_node in enumerate(open_list):
            if sel_node.f < current_node.f:
                current_node = sel_node
                currentIndex = i

        print("\rCurrentnode",current_node.position, current_node.g, current_node.direction, flush=True)
        open_list.pop(currentIndex)
        closedList.append(current_node)

        if current_node.position == end_node.position:
            print("At Goal")
            current = current_node
            total_heat = current_node.g
            while current is not None:
                path.append((current.position, current.g))
                current = current.parent
            break

        # Generate children
        children = []
        possible_dir = [(x, length) for length in range(1,4) for x in [(0, -1), (0, 1), (-1, 0), (1, 0)]]

        prev_path = []
        prev_dirs = {x:0 for x in possible_dir}
        current = current_node

        for new_position in possible_dir:
            node_position = (
                current_node.position[0] + new_position[0][0]*new_position[1],
                current_node.position[1] + new_position[0][1]*new_position[1])

            if current_node.parent:
                if(current_node.parent.position == node_position):
                    continue

            if(current_node.direction):
                if(current_node.direction[0] == new_position[0] or (current_node.direction[0][0]*-1, current_node.direction[0][1]*-1) == new_position[0]):
                    continue
            
            if node_position[0] > (len(lines) - 1) or node_position[1] > (len(lines[0]) - 1) or node_position[0] < 0 or node_position[1] < 0:
                continue

            new_node = node(current_node, node_position, new_position)
            children.append(new_node)
                
        for child in children:
            if child in closedList:
                continue

            # print("\nSumming G for", child)
            g = current_node.g
            for i in range(1, child.direction[1]+1):
                g += int(lines[child.parent.position[0]+(i*child.direction[0][0])][child.parent.position[1]+(i*child.direction[0][1])])
                # print(g)
            child.g = g
            child.h = 0
            child.f = child.g + child.h

            if child in open_list:
                continue

            open_list.append(child)

    # print(path)
    grid = [["..." for x in line] for y in lines]
    for step in path:
        grid[step[0][0]][step[0][1]] = "%3d" % step[1]
        print(step)
    print("Total Heat Loss:", total_heat)

    for line in grid:
        print(line)

    return total_heat