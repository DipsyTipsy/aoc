from solver import utils
import re
from collections import defaultdict

def press_button(button, cur_state):
    n_state = [x for x in cur_state]
    for val in button:
        if cur_state[val] == ".":
            n_state[val] = "#"
        else:
            n_state[val] = "."

    return "".join(n_state)

def go_deeper(pos_states, depth, visited, target_state, buttons):
    while target_state not in pos_states:
            cur_state = pos_states
            # print(depth, cur_state)
            pos = []

            for s in cur_state:
                for button in buttons:
                    result = press_button(button, s)
                    # print("Pressing: ", depth, button, "from ", s, "to ", result)
                    if result == target_state:
                        # print("target_found: ", depth+1)
                        return depth + 1
                    if not result in visited:
                        pos.append(result)
                        visited.add(result)

            pos_states = pos
            
            
            depth += 1
            if depth > 100:
                print(pos_states)
                break
@utils.performance_timer
def solve(input_file: str):
    lines = utils.read_lines(input_file)

    presses = 0 
    for line in lines:
        # print(line)
        target_state = re.match(r"\[([^\]]+)", line).group(1)
        cur_state = "."*len(target_state)
        buttons = [[int(y) for y in x.split(",")] for x in re.findall(r"\(([^\)]+)", line)]

        pos_states = [cur_state]
        min_presses = None
        depth = 0
        visited = set()
        result = go_deeper(pos_states, depth, visited, target_state, buttons)
        # print(result)
        presses += result
        
    return presses
        
