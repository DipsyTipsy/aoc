from solver import utils

class node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # G is the distance between the current node and the start node.
        self.g = 0
        # H is the heuristic — estimated distance from the current node to the end node.
        self.h = 0
        # F is the total cost of the node
        self.f = 0
    def __repr__(self):
        return f"node(positon={self.position},f={self.f})"
    def __eq__(self, other):
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

    while len(open_list) > 0 and failsafe < 10000:
        failsafe += 1
        current_node = open_list[0]
        currentIndex = 0
        for i, sel_node in enumerate(open_list):
            if sel_node.f < current_node.f:
                current_node = sel_node
                currentIndex = i
        # print("Currentnode, OpenList\n",current_node.position, open_list)
        print("Currentnode\n",current_node.position, current_node.g)
        open_list.pop(currentIndex)

        if current_node == end_node:
            print("At Goal")
            current = current_node
            while current is not None:
                path.append((current.position, lines[current.position[0]][current.position[1]]))
                current = current.parent
            break

        # Generate children
        children = []
        direction = (0,0)
        if current_node.parent:
            if current_node.parent.parent:
                direction = (current_node - current_node.parent.parent)
                direction = (-int(direction[0]/2), -int(direction[1]/2))

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if current_node.parent:
                if new_position == current_node.parent.position:
                    continue
                if new_position == direction:
                    print(new_position, direction)
                    continue
            
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1])
            
            if node_position[0] > (len(lines) - 1) or node_position[1] > (len(lines[0]) - 1) or node_position[0] < 0 or node_position[1] < 0:
                continue

            new_node = node(current_node, node_position)
            children.append(new_node)

        current_path = []
        current = current_node
        while current is not None:
            current_path.append((current.position, lines[current.position[0]][current.position[1]]))
            current = current.parent
        grid = [["." for x in line] for y in lines]
        for step in current_path:
            grid[step[0][0]][step[0][1]] = "X"
        for line in grid:
            print(line)
        
        for child in children:
            if child in closedList:
                continue

            child.g = current_node.g + int(lines[child.position[0]][child.position[1]])
            #child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.h = 0
            child.f = child.g + child.h

            if child in open_list:
                continue

            open_list.append(child)
        # for item in open_list:
        #     print(item)

        
    heat_loss = []
    grid = [["." for x in line] for y in lines]
    for step in path:
        heat_loss.append(int(step[1]))
        grid[step[0][0]][step[0][1]] = "X"
    print("Total Heat Loss:", sum(heat_loss))

    for line in grid:
        print(line)