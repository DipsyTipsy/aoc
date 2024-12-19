from solver import utils
from itertools import permutations


def solve(input_file: str):
    lines = utils.read_lines(input_file)
    print(lines)
    patterns = sorted(set(lines[0].split(", ")), key=len)[::-1]

    targets = lines[2:]
    print(patterns, targets)

    posisble = []

    for target in targets:
        _target = target
        _patterns = set((x for x in patterns if x in target))
        for perm in permutations(_patterns):
            print(perm)
            _target = target
            for pattern in perm:
                _target =  _target.replace(pattern, "")
                if len(_target) == 0:
                    posisble.append(target)
                    break
            if len(_target) == 0:
                break

        print(target, len(_target), _target)
    
    print(posisble)
    return len(posisble)
