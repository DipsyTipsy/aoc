from solver import utils
from itertools import permutations
import re


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print(lines)
    patterns = sorted(set(lines[0].split(", ")), key=len)[::-1]

    targets = lines[2:]
    print(patterns, targets)

    possible = set()

    for target in targets:
        print(target)
        _patterns = set((x for x in patterns if x in target))
        hits = [0]*len(target)
        for pattern in _patterns:
            print(pattern)
            indexes = [x.span() for x in re.finditer(pattern, target)]
            for start,end in indexes:
                for i in range(start,end):
                    print(i)
                    hits[i] += 1
            print(pattern, indexes)
        
        sub_pattern = "|".join(_patterns)
        sub_target = re.sub(sub_pattern, " ",target)
        print(sub_target)

        print(hits)

        if all([x > 0 for x in hits]):
            print("Possible")
            possible.add(target)
        else:
            print("Impossible")
        print()
    
    print(possible)
    # return len(possible)
