from solver import utils
from itertools import permutations, product

numeric = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, "A"]
]

directional = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

def move(current, target_pos):
    presses = [] 
    delta = (target_pos[0] - current[0], target_pos[1] - current[1])
    #print("Moving from", current, "To", target_pos, "Delta", delta, end=" ")

    if delta[0] == 0 and delta[1] == 0:
        presses.append("")

    if delta[1] > 0:
        presses += delta[1]*">"
    elif delta[1] < 0:
        presses += abs(delta[1])*"<"

    if delta[0] > 0:
        presses += delta[0]*"v"
    elif delta[0] < 0:
        presses += abs(delta[0])*"^"
    
    return ["".join(x)+"A" for x in list(permutations(presses))]

def get_presses(start, targets, map, _type):
    presses = []
    current = start
    for target in targets:
        target_pos = map[target]
        cur_presses = move(current, target_pos)
        if _type == "numeric":
            match current:
                case (0,0):
                    cur_presses = [x for x in cur_presses if x not in ["vvv>A", "vvv>>A"]]
                case (1,0):
                    cur_presses = [x for x in cur_presses if x not in ["vv>A", "vv>>A"]]
                case (2,0):
                    cur_presses = [x for x in cur_presses if x not in ["v>A", "v>>A"]]
                case (3,1):
                    cur_presses = [x for x in cur_presses if x not in ["<^A", "<^^A", "<^^^A"]]
                case (3,2):
                    cur_presses = [x for x in cur_presses if x not in ["<<^A", "<<^^A", "<<^^^A"]]

        elif _type == "directional":
            match current:
                case (0,2):
                    cur_presses = [x for x in cur_presses if x not in ["<<vA"]]
                case (0,1):
                    cur_presses = [x for x in cur_presses if x not in ["<vA"]]
                case (1,0):
                    cur_presses = [x for x in cur_presses if x not in ["^>>A", "^>A"]]

        presses.append(cur_presses)
        current = target_pos
    # print("Return", presses)
    return presses

def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print()
    n_start = (3, 2)
    d_start = (0, 2)

    numeric_map = {}
    for y, l in enumerate(numeric):
        for x, ch in enumerate(l):
            numeric_map[str(ch)] = (y,x)
    print(numeric_map)

    directional_map = {}
    for y, l in enumerate(directional):
        for x, ch in enumerate(l):
            directional_map[str(ch)] = (y,x)
    print(directional_map)

    total_complexity = []
    for line in lines:
        print()
        # Level 1
        print("R1: Trying to type", line)
        r1 = get_presses(n_start, line, numeric_map, "numeric")
        r1 = set(["".join(x) for x in list(product(*r1))])

        # Level 2
        r2 = set()
        current_shortest = 9999999
        for target in r1:
            print("R2: Trying to type", target, len(target))
            presses = get_presses(d_start, target, directional_map, "directional")
            [r2.add("".join(x)) for x in product(*presses)]
            press = "".join([x[0] for x in presses])
            if len(press) < current_shortest:
                current_shortest = len(press)
            print(press, current_shortest)

        min_len = min(len(x) for x in r2)
        r2 = set([x for x in r2 if len(x) == min_len])
        # for presses in r2:
            # print(len(presses), "Presses", presses)
        # print(len(r2))

        # Level 3
        current_shortest = 999999
        current_longest = 0
        current_press = ""
        num_short = 0
        for target in r2:
            print("R3: Trying to type", target, len(target), "Current_shortest", current_shortest)
            r3 = set()
            presses = get_presses(d_start, target, directional_map, "directional")
            press = "".join([x[0] for x in presses])
            #[r3.add("".join(x)) for x in product(*presses)]
            
            if len(press) < current_shortest:
                current_shortest = len(press)
                current_press = press

            # print(press, len(press))
            # [r3.add("".join(x)) for x in product(*presses) if len("".join(x)) < current_shortest]
            # print(len(r3))
            # for press in r3:
            #     press_len = len(press)
            #     if press_len < current_shortest:
            #         num_short = 0
            #         current_shortest = press_len
            #         current_press = press
            #     elif press_len == current_shortest:
            #         num_short += 1
                
            #     if press_len > current_longest:
            #         current_longest = press_len
            # if current_longest != current_shortest:
            #     break

        
        print(line, current_shortest, current_press)
        total_complexity.append([current_shortest, int(line[:-1])])
    
    print(total_complexity)
    return sum([x[0] * x[1] for x in total_complexity])