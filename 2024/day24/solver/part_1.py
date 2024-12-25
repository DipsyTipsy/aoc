from solver import utils
import re
from collections import defaultdict

def process(a,operation, b,dest,wires):
    a_val = wires.get(a)
    b_val = wires.get(b)
    if a_val == None or b_val == None:
        return None
    else:
        match operation:
            case "AND":
                wires[dest] = a_val and b_val
            case "OR":
                wires[dest] = a_val or b_val
            case "XOR":
                wires[dest] = a_val ^ b_val
        return True

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print()
    wires = {}
    queue = []

    for line in lines:
        if ":" in line:
            wire, state= re.findall(r"(\S+): (\d)", line)[0]
            wires[wire] = int(state)
        elif "->" in line:
            a, operation, b, dest = re.findall(r"(\S+) (\S+) (\S+) -> (\S+)", line)[0]
            if not process(a,operation,b,dest,wires):
                queue.append((a,operation,b,dest))

    steps = 0
    while len(queue) > 0 and steps < 10000:
        a, operation, b, dest = queue.pop(0)
        if not process(a,operation,b,dest,wires):
            queue.append((a,operation,b,dest))
        steps += 1

    
    result = ""
    for wire, value in sorted(wires.items()):
        if "z" in wire:
            result += str(value)
    
    result = result[::-1]
    result_value = int(result, 2)
    return result_value
