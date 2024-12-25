from solver import utils
from collections import defaultdict


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    network_map = defaultdict(list)
    computers = set()

    for line in lines:
        a, b = line.split("-")
        network_map[a] += [b]
        network_map[b] += [a]
        computers.add(a)
        computers.add(b)
    
    sets = set()
    for comp in computers:
        for peer in network_map[comp]:
            for x in network_map[peer]:
                if x in network_map[comp]:
                    sets.add(tuple(sorted([comp, peer, x])))
                    
                
    desired_sets = set()
    for pair in sets:
        if any([x.startswith("t") for x in pair]):
            desired_sets.add(pair)
    print(len(sets))
    print(len(desired_sets))

    return len(desired_sets)