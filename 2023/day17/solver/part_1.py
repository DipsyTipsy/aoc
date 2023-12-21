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
            return all([self.position == other.position, self.direction[0] == other.direction[0], self.direction[1]==other.direction[1]])
        return self.position == other.position
    def __sub__(self, other):
        return (other.position[0] - self.position[0], other.position[1] - self.position[1])

def solve(input_file: str):
    lines = [list(x) for x in utils.read_lines(input_file)]

    optimal_path = [((12, 12), '0'), ((12, 11), '0'), ((11, 11), '0'), ((10, 11), '0'), ((10, 12), '0'), ((9, 12), '0'), ((8, 12), '0'), ((7, 12), '0'), ((7, 11), '0'), ((6, 11), '0'), ((5, 11), '0'), ((4, 11), '0'), ((4, 10), '0'), ((3, 10), '0'), ((2, 10), '0'), ((2, 9), '0'), ((2, 8), '0'), ((1, 8), '0'), ((0, 8), '0'), ((0, 7), '0'), ((0, 6), '0'), ((0, 5), '0'), ((1, 5), '0'), ((1, 4), '0'), ((1, 3), '0'), ((1, 2), '0'), ((0, 2), '0'), ((0, 1), '0'), ((0, 0), '2')]
    optimal_path = [x[0] for x in optimal_path]

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

    while len(open_list) > 0 and failsafe < 500000:
        failsafe += 1
        current_node = open_list[0]
        currentIndex = 0
        for i, sel_node in enumerate(open_list):
            if sel_node.f < current_node.f:
                current_node = sel_node
                currentIndex = i
        # print("Currentnode, OpenList\n",current_node.position, open_list)
        print("Currentnode\n",current_node.position, current_node.g, current_node.direction)
        open_list.pop(currentIndex)
        closedList.append(current_node)

        if current_node.position == end_node.position:
            print("At Goal")
            current = current_node
            while current is not None:
                path.append((current.position, lines[current.position[0]][current.position[1]]))
                current = current.parent
            break

        # Generate children
        children = []
        possible_dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        prev_path = []
        prev_dirs = {x:0 for x in possible_dir}
        current = current_node

        for new_position in possible_dir:
            new_direction = [new_position, 0]

            if current_node.direction:
                if new_position == current_node.direction[0]:
                    new_direction[1] += max([current_node.direction[1], 0]) +1

            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1])
            
            if current_node.parent:
                if(current_node.parent.position == node_position):
                    continue
            
            if node_position[0] > (len(lines) - 1) or node_position[1] > (len(lines[0]) - 1) or node_position[0] < 0 or node_position[1] < 0 or new_direction[1] >=3:
                continue

            # if node_position in optimal_path:
                # new_node = node(current_node, node_position, new_position)
                # children.append(new_node)
# 
            new_node = node(current_node, node_position, new_direction)
            children.append(new_node)
                
        for child in children:
            if child in closedList:
                continue

            child.g = current_node.g + int(lines[child.position[0]][child.position[1]])
            # child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.h = 0
            child.f = child.g + child.h

            if child in open_list:
                continue

            open_list.append(child)

        # current_path = []
        # current = current_node
        # while current is not None:
        #     current_path.append((current.position, current.g))
        #     current = current.parent
        # grid = [["..." for x in line] for y in lines]
        # for item in open_list:
        #     grid[item.position[0]][item.position[1]] = "%3s" % "P"
        #     print(item)
        # for item in closedList:
        #     grid[item.position[0]][item.position[1]] = "%3s" % "C"
        # for step in current_path:
        #     grid[step[0][0]][step[0][1]] = "%3d" % step[1]
        # for line in grid:
        #     print(line)
        
    heat_loss = []
    grid = [["." for x in line] for y in lines]
    for step in path:
        heat_loss.append(int(step[1]))
        grid[step[0][0]][step[0][1]] = step[1]
        print(step)
    print("Total Heat Loss:", sum(heat_loss))

    for line in grid:
        print(line)

    return sum(heat_loss) - int(lines[start[0]][start[1]])