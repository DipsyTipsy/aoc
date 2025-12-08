from solver import utils
import math
from collections import defaultdict

def cartesian(a,b):
    return math.sqrt(
        pow(a[0]-b[0], 2) +
        pow(a[1]-b[1], 2) +
        pow(a[2]-b[2], 2)
        )


def solve(input_file: str,connections):
    print()
    lines = utils.read_lines(input_file)
    boxes = [tuple([int(x) for x in line.split(",")]) for line in lines]

    distances = {}
    circuts = []
    for box in boxes:
        for box_ in boxes:
            if box != box_:
                distances[cartesian(box, box_)] = (box, box_)
    
    num_connections = 0
    for i in range(connections):
        to_connect = distances.pop(min(distances))
        connected = False
        pos_circut = []
        for j, circut in enumerate(circuts):
            if any(box in circut for box in to_connect):
                pos_circut.append(j)

        if len(pos_circut) == 1:
            circuts[pos_circut[0]].add(to_connect[0])
            circuts[pos_circut[0]].add(to_connect[1])
            connected = True
            num_connections += 1
        elif len(pos_circut) > 1 and not connected:
            to_combine = []
            for cir in sorted(pos_circut, reverse=True):
                to_combine.append(circuts.pop(cir))
            n_circut = to_combine[0].union(to_combine[1])

            circuts.append(n_circut)
            connected = True
            num_connections += 1
        elif not connected and not len(pos_circut) > 0:
            circuts.append(set(to_connect))
            num_connections += 1

    circut_len = []
    box_count = defaultdict(int)
    for circut in circuts:
        circut_len.append(len(circut))
        for box in circut:
            box_count[box] +=1


    for box in box_count.items():
        if box[1] > 1:
            print(box)
    print(sorted(circut_len, reverse=True))
    
    return math.prod(sorted(circut_len, reverse=True)[:3])