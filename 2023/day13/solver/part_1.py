from solver import utils
import numpy as np


def solve(input_file: str):
    lines = "\n".join(utils.read_lines(input_file))
    patterns = [x.split("\n") for x in lines.split("\n\n")]
    print()

    #for pattern in patterns:
    #    print()
    #    for line in pattern:
    #        print(line)
    

    print("\nSolve")
    sums = []

    def find_mirror(pattern, multiplier):
        pattern_len = len(pattern)
        for i in range(len(pattern)-1):
            if pattern[i] == pattern[i+1]:
                top = pattern[:i+1]
                bottom = pattern[i+1:]

                len_top = len(top)
                len_bottom = len(bottom)
                if len_top != len_bottom:
                    if len_top > len_bottom:
                        top = top[len_top-len_bottom:]
                    if len_top < len_bottom:
                        bottom = bottom[:-(len_bottom-len_top)]

                if top == list(reversed(bottom)):
                    return multiplier*(i+1)
        return 0

    for pattern in patterns:
        print()
        sums.append(find_mirror(pattern, 100))
        rotated = list(["".join(x) for x in zip(*pattern[::-1])])
        sums.append(find_mirror(rotated, 1))

        for line in pattern:
            print(line)
        print(sums[-2:])

    print(print(sums)) 
    return sum(sums)
