from solver import utils
import re, math
from collections import defaultdict
import numpy as np
from itertools import combinations, combinations_with_replacement, permutations, product


def press_button(button, cur_state, target_state):
    n_state = cur_state+button
    return n_state

def calc_distance(cur_state, target_state):
    return np.sum(target_state-cur_state)

def go_deeper(pos_states, distance, depth, target_state, buttons):
    if depth > 20000:
        return

    # if all([str(x) in visited for x in pos_states]) and depth > 0:
    #     print("dont bother")
    #     return

    cur_state = pos_states
    if len(cur_state) == 0:
        return None
    print("\r depth:", depth, distance,len(cur_state),"                ", end="")
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
    # filter_ = [not str(x) in visited for x in pos_states]
    # pos_states = pos_states[filter_]

    distances = np.array([calc_distance(x, target_state) for x in pos_states])
    while len(distances) > 0:
        # print()
        # filter_ = [not hash(str(x)) in visited for x in pos_states]
        # print("CHECKING", len(distances))
        if len(distances) > 0:
            # [visited.add(str(x)) for x in cur_state]
            min_distance = np.min(distances)
            d = go_deeper(pos_states[distances == np.min(distances)],min_distance, depth+1, target_state, buttons)
            if d:
                return d
            else:
                # visited.add(hash(str(pos_states)))
                # print("Moving min", d, pos_states)
                pos_states = pos_states[distances > min(distances)] 
                distances = distances[distances > min(distances)]
                # filter_ = [not hash(str(x)) in visited for x in pos_states]
                # pos_states[filter_]
                # distances[filter_]
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
        # print(max(next), cur_min, min([distance for distance in queue.keys()]), len(visited), len(queue))
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

def find_presses(buttons, target_levels):
    max_ = max(target_levels)
    min_ = min(target_levels)
    l_buttons = len(buttons)
    


    cur_state = [np.zeros(len(target_levels))]
    print(type(cur_state))
    
    # for i in range(max_, max_*2):
    #     print(i)
    #     for j in range(0, i):
    #         print(j)
    print()
    for i in range(10):
        print(i, len(cur_state))
        n_cur = []
        for s in cur_state:
            # print(type(s), s.shape)
            s = s + buttons
            # s = s.tolist()
            # print("s",s)
            for x in s:
                n_cur.append(x)
        cur_state = np.unique(n_cur, axis=1)
        cur_state = cur_state[[np.all(x<=target_levels) for x in cur_state]]
        cur_state = cur_state[0][:10]
        # print(cur_state)
        print()


        cur_state = n_cur 
        # print("cur", cur_state)
        # # cur_state = np.unique([s+buttons for s in cur_state], axis=1)

        # print(len(cur_state), cur_state)
        
        if any([np.all(x == target_levels) for x in cur_state]):
            return i
        # print(cur_state)
    
        #     print("num_buttons", j, "/", l_buttons-1, "total_presses", i)


        #     (np.sum(combo) for combo in combinations(buttons, j))


        #     for combo in combinations(buttons, j):
        #         # print(sum(combo), target_levels)
        #         # s_combo = sum(combo)
        #         print(sum(combo), i, max_, min_)
        #         # return 0
        #         print(np.sum(combo))

        #         # correct = (np.sum(sum(n_cur) == target_levels) for n_cur in combinations_with_replacement(combo, i))
        #         # # print("num_correct", correct)
        #         # if any([x == len(target_levels) for x in correct]):
        #         #     return i
                
        #             # n_correct = np.sum([sum(n_cur) == target_levels])
        #             # if n_correct == len(target_levels):
        #             #     print("Lucky break!")
        #             #     return i
        #             # print(n_correct)

        # if any(cur >= target_levels):
        #     rem_buttons = buttons #[x for x in buttons if any(x != button)]
        #     room = i

        #     print(max_, room)
        #     if room > 0:
        #         print("Testing combos", room, max_)
        #         for other in combinations_with_replacement(rem_buttons, room):
        #             n_cur = sum(other)
        #             n_correct = np.sum([n_cur == target_levels])

        #             if n_correct == len(target_levels):
        #                 print("Lucky break!")
        #                 return i

        #             if n_correct > num_correct:
        #                 num_correct = n_correct
        #                 print("better", num_correct,  len(target_levels))
        #                 # print("ncurr", n_cur, target_levels)
            

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
        
        print(cur_state, target_levels, buttons)

        # presses += find_presses(buttons, target_levels)
                
                # print(sum(button), button)

        depth = 0
        pos_states = np.array(cur_state)
        pos_states = np.vstack((pos_states, pos_states))
        result = go_deeper(pos_states, 10000, depth, target_levels, buttons)
        presses += result

        # presses += search(cur_state, target_levels, buttons)
        
    return presses