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

def run_operations(wires, operations):
    queue = []
    steps = 0
    for a,operation,b,dest in operations:
        if not process(a,operation,b,dest, wires):
            queue.append((a,operation,b,dest))

    while len(queue) > 0 and steps < 10000:
        a, operation, b, dest = queue.pop(0)
        if not process(a,operation,b,dest,wires):
            queue.append((a,operation,b,dest))
        steps += 1

    result = ""
    for wire, value in sorted(wires.items()):
        # print(wire,value)
        if "z" in wire:
            result += str(value)

    return result
 

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print()
    wires = {}
    queue = []

    operations = []

    for line in lines:
        if ":" in line:
            wire, state= re.findall(r"(\S+): (\d)", line)[0]
            wires[wire] = int(state)
        elif "->" in line:
            a, operation, b, dest = re.findall(r"(\S+) (\S+) (\S+) -> (\S+)", line)[0]
            operations.append((a,operation,b,dest))
    
    initial_wires = wires.copy()
    initial_operations = operations.copy()

    x = ""
    y = ""
    for wire, value in sorted(wires.items()):
        print(wire,value)
        if "x" in wire:
            x += str(value)
        elif "y" in wire:
            y += str(value)
    x = x[::-1]
    y = y[::-1]
    x_val  = int(x,2)
    y_val = int(y,2)
    correct_value = x_val + y_val 
    correct = format(correct_value, "b")
    result = None
    checked_operations = set()
    latest_swap = []
    closest = 9999999999
    checked_value = defaultdict(int)

    while result != correct and str(sorted([(dest,a,b) for a,operation,b,dest in operations])) not in checked_operations:

        result = run_operations(wires, operations)
        result = result[::-1]
        result_value = int(result, 2)

        if checked_value.get(result_value,0) > 10:
            print("Repeat", print(checked_value, result_value))
            break

        checked_value[result_value] += 1
        diff  = abs(correct_value - result_value)
        if diff < closest:
            closest = diff

        if result_value == correct_value:
            break
        checked_operations.add(str(sorted([(dest,a,b) for a,operation,b,dest in operations])))
        # print(f"Operation: {x_val}({x}) + {y_val}({y}) = {result_value}({result}),  Should be {correct_value}({correct})")

        wrong_indexes = []
        _correct = correct[::-1]
        for i,bit in enumerate(result[::-1]):
            if i in range(len(_correct)):
        #        print(bit, _correct[i], end=" ")
                if bit != _correct[i]:
        #            print("WRONG", end="")
                    wrong_indexes.append(i)
        #        print()

        latest_swap = []
      #  print(wrong_indexes)
        _operations = operations.copy()
        for index in range(1, len(wrong_indexes),2):
            a,operation,b,dest = _operations[wrong_indexes[index]]
            instance_a = _operations[wrong_indexes[index]]
            _a,_operation,_b,_dest = _operations[wrong_indexes[index-1]]
            instance_b = _operations[wrong_indexes[index-1]]
            operations.remove(instance_a)
            operations.remove(instance_b)
            operations.append((a,operation,b, _dest))
            operations.append((_a,_operation,_b, dest))
            # print("Swapping", wrong_indexes[index], dest, wrong_indexes[index-1], _dest)
            latest_swap.append(dest)
            latest_swap.append(_dest)

        if len(checked_operations) > 10000000:
            break
    
    print(latest_swap)
    print(closest)