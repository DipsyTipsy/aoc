from solver import utils
import re
from collections import defaultdict
import numpy as np

def press_button(button, cur_state, target_state):
    n_state = cur_state+button
    return n_state

def calc_distance(cur_state, target_state):
    return np.sum(target_state-cur_state)

def go_deeper(pos_states, depth, target_state, buttons, visited):
    if depth > 20000:
        return

    if all([str(x) in visited for x in pos_states]) and depth > 0:
        print("dont bother")
        return

    cur_state = pos_states
    if len(cur_state) == 0:
        return None
    print("\r depth:", depth, len(visited), len(cur_state),"                ", end="")
    pos = None

    for button in buttons:
        result = press_button(button, cur_state, target_state)
        if np.any(np.all(result == target_state, axis=1)):
            # print()
            print("target_found: ", depth+1)
            # print(result, target_state)
            return depth + 1


        # print("filtered", result[[np.all(x <= target_state) for x in result.tolist()]])
        # filter_ = [not hash(str(x)) in visited for x in result]
        # print("Result", result, filter_)
        # result = result[filter_]
        # if len(result) > 0:
        if not type(pos) == np.ndarray:
            pos = result[[np.all(x <= target_state) for x in result.tolist()]]
        else:
            pos = np.vstack((pos, result[np.all(result <= target_state, axis=1)]))
        
    if not type(pos) == np.ndarray:
        return

    pos_states = np.unique(pos, axis=0)
    filter_ = [not str(x) in visited for x in pos_states]
    pos_states = pos_states[filter_]

    distances = np.array([calc_distance(x, target_state) for x in pos_states])
    while len(distances) > 0:
        # print()
        filter_ = [not hash(str(x)) in visited for x in pos_states]
        # print("CHECKING", len(distances))
        if len(distances) > 0:
            [visited.add(str(x)) for x in cur_state]
            d = go_deeper(pos_states[distances == np.min(distances)], depth+1, target_state, buttons, visited)
            if d:
                return d
            else:
                # visited.add(hash(str(pos_states)))
                # print("Moving min", d, pos_states)
                pos_states = pos_states[distances > min(distances)] 
                distances = distances[distances > min(distances)]
                filter_ = [not hash(str(x)) in visited for x in pos_states]
                pos_states[filter_]
                distances[filter_]
        else:
            print("All dist checked")
            return None
    return
    depth += 1

def search(pos_states, target_state, buttons):
    distance = calc_distance(pos_states, target_state)
    queue = defaultdict(list)
    queue[distance] = [pos_states]
    visited = {
        str(pos_states): 0
    }
    print("Initial Queue", queue, distance)


    while len(queue) > 0:
        cur_min = min([distance for distance in queue.keys()])
        next = queue[cur_min].pop(0)
        depth = visited[str(next)]
        print(max(next), cur_min, min([distance for distance in queue.keys()]), len(visited), len(queue))
        if len(queue[cur_min]) == 0:
            queue.pop(cur_min)


        for button in buttons:
            result = press_button(button, next, target_state)
            if all(result == target_state):
                print("hit")
                return depth+1
            if str(result) not in visited and all(result <= target_state):
                distance = calc_distance(result, target_state)
                queue[distance].append(result)
                visited[str(result)] = min([depth+1, visited.get(str(result), np.inf)])
                # print(min([depth+1, visited.get(str(next), np.inf)]), next)


        visited[str(next)] = min([depth+1, visited.get(str(next), np.inf)])
        # if len(queue) == 3 and len(visited) > 250:
        #     for k,v in queue.items():
        #         print(k, len(v), type(v))
        #     return

@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)

    presses = 0 
    for line in lines:
        print(line)
        buttons = [[int(y) for y in x.split(",")] for x in re.findall(r"\(([^\)]+)", line)]
        target_levels = np.array([[int(y) for y in x.split(",")] for x in re.findall(r"\{([^\}]+)", line)][0])
        cur_state = np.zeros(len(target_levels))

        n_buttons = []
        for button in buttons:
            cur_button = np.zeros(len(target_levels))
            for val in button:
                cur_button[val] = 1
            n_buttons.append(cur_button)
        
        buttons = n_buttons
        
        print(cur_state, target_levels)

        depth = 0
        # visited = set()
        # pos_states = np.array(cur_state)
        # pos_states = np.vstack((pos_states, pos_states))
        # result = go_deeper(pos_states, depth, target_levels, buttons, visited)
        # presses += result
        presses += search(cur_state, target_levels, buttons)
        
    return presses