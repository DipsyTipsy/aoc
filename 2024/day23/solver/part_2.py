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


    def find_peers(comp, current_set):
        if comp in current_set:
            return current_set

        current_set.add(comp)

        all_peers = []
        for peer in network_map[comp]:
            if all([peer in network_map[x] for x in current_set]):
                current_set.add(peer)
                peers = find_peers(peer, current_set)
                all_peers.append(peers)
        return all_peers
    
    sets = set()
    for comp in computers:
        c_set = set()
        [sets.add(tuple(sorted(x))) for x in find_peers(comp, c_set)]
    
    return ",".join(sorted(sets, key=len)[-1])